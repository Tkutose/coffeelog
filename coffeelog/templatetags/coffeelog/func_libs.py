from coffeelog.models import Log, Store
from django import template

register = template.Library()

@register.filter(name ="change_star")
def change_star(column):
    '''
    値を受け取り、★１～５に変換して返す
    '''
    star = ''  

    for i in range(column):
        star += '★'

    for i in range((5-column)):
        star += '☆'

    return star
    


@register.filter(name ="hot_or_ice")
def out_temperature(bool):
    '''
    boolean値のhotを文字化して返す
    '''
    if bool:
        return 'HOT'
    else:
        return 'ICE'

@register.filter(name ='form_add_class')
def out_form_item(elem, block_name):
    '''
    formの要素と親ブロックのクラス名を受け取って
    BEMに基づいたクラス付けをして返す
    '''

    return elem.as_widget(attrs={'class': block_name+ '__' + elem.name})
