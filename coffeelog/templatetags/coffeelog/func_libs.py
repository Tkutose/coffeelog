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
    if bool:
        return 'HOT'
    else:
        return 'ICE'
