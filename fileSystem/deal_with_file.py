from doctest import DocFileCase
from operator import ne
import os
from pydoc import doc
import re
import yaml
from docx import Document
import random


def delInTable(tables, kwd='__删除整行__'):
    if tables == []:
        return
    for t, table in enumerate(tables):
        for r, row in enumerate(table.rows):  # 遍历表格的行
            for c, cell in enumerate(row.cells):  # 遍历每一行的列
                text = cell.text
                if kwd in text:
                    row._element.getparent().remove(row._element)
                    break


def del_rows(doc_path, kwd='__删除整行__'):
    if doc_path is None:
        return
    document = Document(doc_path)
    delInTable(document.tables, kwd)
    for t, table in enumerate(document.tables):
        for r, row in enumerate(table.rows):  # 遍历表格的行
            for c, cell in enumerate(row.cells):  # 遍历每一行的列
                delInTable(cell.tables, kwd)
    document.save(doc_path)


def delTextInTable(tables, kwd='__删除文本__'):
    if tables == []:
        return
    del_list = []
    for t, table in enumerate(tables):  # 遍历所有表格，这个模板里有3个表格
        for r, row in enumerate(table.rows):  # 遍历表格的行
            for c, cell in enumerate(row.cells):  # 遍历每一行的列
                text = cell.text
                if kwd in text:
                    del_list.append((t, r))
                    break

    for t, r in set(del_list):
        row = tables[t].rows[r]
        for cell in row.cells:
            cell.text = ""


def del_text(doc_path, kwd='__删除文本__'):
    if doc_path is None:
        return
    document = Document(doc_path)
    delTextInTable(document.tables, kwd)
    for t, table in enumerate(document.tables):  # 遍历所有表格，这个模板里有3个表格
        for r, row in enumerate(table.rows):  # 遍历表格的行
            for c, cell in enumerate(row.cells):  # 遍历每一行的列
                delTextInTable(cell.tables, kwd)

    document.save(doc_path)


def GetDictionary(yamlFile):
    """
    从yamlFile中读取替换字典
    """
    with open(yamlFile, 'r', encoding='utf8') as y:
        return yaml.safe_load(y.read())


def ReplaceInRuns(paragraph, replaceDict: dict, paragraphType):
    """
    将paragraph中所有runs根据replaceDict进行替换
    """
    text = ""
    if paragraphType == "plain" or "header":
        for run in paragraph.runs:
            if text == "":
                if run.text.count("__") % 2 != 0:  # 发生了截断
                    text = run.text
                    run.text = ""
                    continue
            else:
                run.text = text + run.text
                if run.text.count("__") % 2 != 0:  # 发生了截断
                    text = run.text
                    run.text = ""
                    continue
            text = ""
            for old, new in replaceDict.items():
                # 进行替换
                if old in run.text:
                    if "随机日期" in old:
                        start, end = new.split('-')
                        new = str(random.randint(int(start), int(end)))
                    if "__是否有空压机__" in old and new == '否':
                        return 1
                    if ("产品批号__" in old or "产品订货时间__" in old):
                        matchObj = re.search(r'__[\u4e00-\u9fa5|0-9]*__', old, re.M | re.I)
                        key1 = matchObj.group()[:12] + "批号__"
                        key2 = matchObj.group()[:12] + "订货时间__"
                        if replaceDict[key1] == '否' and replaceDict[key2] == '否':
                            return 1
                    run.text = run.text.replace(old, new)
    else:
        if paragraphType == "table":
            for run in paragraph.runs:
                text += run.text.strip()
            for old, new in replaceDict.items():
                # 进行替换
                if old in text:
                    if "随机日期" in old:
                        start, end = new.split('-')
                        new = str(random.randint(int(start), int(end)))
                    if "__是否有空压机__" in old and new == '否':
                        return 1
                    if ("产品批号__" in old or "产品订货时间__" in old):
                        matchObj = re.search(r'__[\u4e00-\u9fa5|0-9]*__', old, re.M | re.I)
                        key1 = matchObj.group()[:12] + "批号__"
                        key2 = matchObj.group()[:12] + "订货时间__"
                        if replaceDict[key1] == '否' and replaceDict[key2] == '否':
                            return 1
                    text = text.replace(old, new)
            if text != "":
                paragraph.runs[0].text = text
            for run in paragraph.runs[1:]:
                run.text = ""
    return 0


def ReplaceInTable(tables, replaceDict):
    if tables == []:
        return 0
    for table in tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    flag1 = ReplaceInRuns(paragraph, replaceDict, "table")
                flag2 = ReplaceInTable(cell.tables, replaceDict)
    return flag1 + flag2


def ReplaceIn(docxFile, workdir, replaceDict: dict):
    """
    将docxFile按replaceDict进行全局替换
    """
    if docxFile[-4:] == '.doc':
        print('无法加载doc文件： ', docxFile, '\n请转换成docx类型！')
        return
    else:
        print('正在处理：', docxFile)

    if docxFile.split('/')[-1][:2] == '.~':
        return

    document = Document(docxFile)

    res_home = replaceDict['__企业名称__'] + replaceDict['template_id'].split('-')[2] + '上报信息'
    res_path = os.path.join(workdir, res_home,
                            os.path.relpath(docxFile, os.path.join(workdir, 'templates', replaceDict['template_id'])))
    res_dir = os.path.dirname(res_path)
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)

    # 页眉
    for section in document.sections:
        for paragraph in section.header.paragraphs:
            flag = ReplaceInRuns(paragraph, replaceDict, "header")
            if flag:
                return None

    # 文本段落
    for paragraph in document.paragraphs:
        flag = ReplaceInRuns(paragraph, replaceDict, "plain")
        if flag:
            return None

    # 表格
    flag = ReplaceInTable(document.tables, replaceDict)
    if flag > 0:
        return None

    document.save(res_path)
    return res_path


def ReplaceAll(path: str, workdir: str, replaceDict: dict, delLineDict: dict, delTextDict: dict):
    """
    将path路径下所有word文件按replaceDict进行全局替换
    """
    directories = os.listdir(path)
    folders = [os.path.join(path, i) for i in directories if
               os.path.isdir(os.path.join(path, i)) and not i.startswith('.')]  # 所有非隐藏文件夹
    for folder in folders:
        ReplaceAll(folder, workdir, replaceDict, delLineDict, delTextDict)
    files = [os.path.join(path, i) for i in directories if
             os.path.isfile(os.path.join(path, i)) and os.path.splitext(i)[-1] in ['.doc', '.docx']]  # 所有word文件
    for file in files:
        respath = ReplaceIn(file, workdir, replaceDict)
        if respath == None:
            os.remove(file)
        del_rows(respath)
        del_text(respath)


def ExamInRuns(paragraph, paragraphType):
    """
    将paragraph中所有runs根据replaceDict进行替换
    """
    text = ""
    if paragraphType == "plain" or "header":
        for run in paragraph.runs:
            if run.text.count('__') > 0:
                return 1
    else:
        if paragraphType == "table":
            for run in paragraph.runs:
                text += run.text.strip()
                if '__' in text:
                    return 1
    return 0


def ExamIn(docxFile):
    """
    将docxFile进行是否有__检查
    """
    if docxFile[-4:] == '.doc':
        print('无法加载doc文件： ', docxFile, '\n请转换成docx类型！')
        return
    else:
        print('正在检查：', docxFile)

    if docxFile.split('/')[-1][:2] == '.~':
        return

    document = Document(docxFile)

    # 页眉
    for section in document.sections:
        for paragraph in section.header.paragraphs:
            if ExamInRuns(paragraph, "header") == 1:
                return docxFile

    # 文本段落
    for paragraph in document.paragraphs:
        if ExamInRuns(paragraph, "plain") == 1:
            return docxFile

    # 表格
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if ExamInRuns(paragraph, "table") == 1:
                        return docxFile


def ExamAll(path: str, depth: int):
    """
    将path路径下所有word文件进行是否有__检查
    """
    directories = os.listdir(path)
    undeal_files = []
    folders = [os.path.join(path, i) for i in directories if
               os.path.isdir(os.path.join(path, i)) and not i.startswith('.')]  # 所有非隐藏文件夹
    for folder in folders:
        undeal_files += ExamAll(folder, 1)
    files = [os.path.join(path, i) for i in directories if
             os.path.isfile(os.path.join(path, i)) and os.path.splitext(i)[-1] in ['.doc', '.docx']]  # 所有word文件
    for file in files:
        undeal_files.append(ExamIn(file))
    if depth == 0:
        with open(path + '/undeal.txt', 'w') as f:
            for line in undeal_files:
                if line:
                    f.write(line + '\n')
    return undeal_files


def ReplaceProcess(info_dict, page2=False):
    dictionary = GetDictionary("tagList.yml")
    deltext = GetDictionary("delText.yml")
    delline = GetDictionary('delLine.yml')
    dictionary['template_id'] = info_dict['template_id']
    work_dir = os.path.abspath('.')  # 工作路径

    # 用收集信息更新替换字典
    for key in dictionary.keys():
        if key in info_dict and info_dict[key] != '无' and info_dict[key] != '否':
            dictionary[key] = info_dict[key]
        elif key[2:-2] in info_dict and info_dict[key[2:-2]] != '无' and info_dict[key[2:-2]] != '否':
            dictionary[key] = info_dict[key[2:-2]]
        elif '随机日期' in key:
            continue
        else:
            dictionary[key] = '否'
        if key in ['__特殊过程焊接__', '__特殊过程搅拌__', '__特殊过程薄膜金属化__', '__特殊过程混合__', '__特殊过程挤出__']:
            if info_dict[key] == '是':
                dictionary[key] = ''
        
        if key in delline and dictionary[key] == delline[key]:
            dictionary[key] = '__删除整行__'
        if key in deltext and dictionary[key] == deltext[key]:
            dictionary[key] = '__删除文本__'
    if dictionary['__有无外包过程__'] == '否':
        dictionary['__外包过程表述__'] = ''
        dictionary['__有无外包过程__'] = '无'

    if page2:
        ReplaceAll(os.path.join('templates', dictionary['template_id'], '01管理手册'), work_dir, dictionary, delline,
                   deltext)
        ReplaceAll(os.path.join('templates', dictionary['template_id'], '02程序文件'), work_dir, dictionary, delline,
                   deltext)
    else:
        ReplaceAll(os.path.join('templates', dictionary['template_id']), work_dir, dictionary, delline, deltext)
    res_home = dictionary['__企业名称__'] + dictionary['template_id'].split('-')[2] + '上报信息'
    ExamAll(res_home, 0)
    print('no check !!!!! process done!')

