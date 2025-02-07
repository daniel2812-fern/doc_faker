import json

def key_labelling_template_1(rowdata):
    context = {
            '醫療院所名稱': 'hopitalname_key',
            '醫療院所地址': 'hospitaladdress_key',
            '診治醫師': 'doctorname_key',
            '科別':'department_key',
            '診斷':'diagnose_key',
            '醫囑':'comment_key',
    }
    return context

def key_labelling_template_2(rowdata):
    context = {
            '醫院名稱': 'hopitalname_key',
            '診治醫師': 'doctorname_key',
            '病名及健康功能狀況':'diagnose_key',
    }
    return context

def key_labelling_template_3(rowdata):
    context = {
            '醫師': 'doctorname_key',
            '科別':'department_key',
            '病名':'diagnose_key',
            '證明及醫囑':'comment_key',
    }
    return context

def key_labelling_template_4(rowdata):
    context = {
        '診治醫師': 'doctorname_key',
        '科別':'department_key',
        '病名':'diagnose_key',
        '醫師囑言':'comment_key',
    }
    return context

def value_labelling(rowdata):
    context = {
        rowdata['hospital_name']: 'hopitalname_value',
        rowdata['hospital_address']: 'hospitaladdress_value',
        rowdata['department']:'department_value',
        rowdata['diagnosis']:'diagnose_value',
        rowdata['doctor_comment']:'comment_value',
        rowdata['doctor_name']:'doctorname_value',
    }
    return context

def kie_labelling(templatename,rowdata):
    contextKey = {}
    contextValue = {}
    template_mapping = {
        'template1': key_labelling_template_1,
        'template2': key_labelling_template_2,
        'template3': key_labelling_template_3,
        'template4': key_labelling_template_4
    }
    contextKey = template_mapping.get(templatename, lambda x: {})(rowdata)
    contextValue = value_labelling(rowdata)
    return {**contextKey, **contextValue}

def load_json_to_dict(filename):
    """Load JSON from a file and return as a dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)

def save_label(data, filename):
    """Save dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
