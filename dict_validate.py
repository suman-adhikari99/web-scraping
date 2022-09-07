def validate_string(value):
    return  True if 5<len(value)<100 else False
def validate_digit(value):
    return True if 0<int(value)<100 else False
def validate_bool(value):
    return True if value==True or value==False else False 
def validate_list(value):
    return True if len(value)>0 else False
def validate_dict(value):
    return True if len(value.keys())>0 else False
def default(value):
    return False

validators = {'int': validate_digit,
              'str': validate_string,
              'bool': validate_bool,
              'list': validate_list,
              'dict':validate_dict,
              'tuple':validate_list
              }
def dictionary_validator(dictionary,rule):
    for value in dictionary.values():
        validated=validators.get(((value.__class__.__name__)), default)(value)
        if validated==False:
            return False           
    else:               
        # This else executes only if validated  is NEVER False
        # reached and loop terminated after all iterations.
        return True


dictionary={
    'a':'data intern',
    'b':11,
    'c':[],

}

print(dictionary_validator(dictionary,validators))



