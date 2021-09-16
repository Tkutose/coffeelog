from coffeelog.models import Log, Store
from django import template
from datetime import datetime as dt

register = template.Library()

jp_dict ={
    'bitter':'苦味',
    'acidity':'酸味',
    'smell':'香り',
    'after':'後味',
    'likely':'個人的な好み',
    'store__name':'店名',
    'date':'投稿日'
}

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


@register.filter(name ='log_count')
def out_count_log(counts, store_name):
    '''
    key:店の名前
    value:その店のLog投稿数
    のdictと店の名前を受け取り、投稿数を返す
    '''

    return counts[store_name]


@register.filter(name ='get_col')
def out_column_data(log, col):
    '''
    Logのオブジェクトとカラム名を受け取って
    検索のために辞書型に変換後
    そのカラムの日本語名と値を返す
    '''
    if col=='store__name':
        return ''

    if col=='date':
        return out_jp_col(col)+':'+log.__dict__[col].strftime('%Y/%m/%d')

    return out_jp_col(col)+':'+str(log.__dict__[col])


@register.filter(name ='col_jp')
def out_jp_col(col):
    '''
    カラム名を日本語に変換
    '''

    return jp_dict[col]


@register.filter(name ='cut_note')
def cut_str(str):
    '''
    備考欄の文字数を制限し、一定文字以上は...に変換
    '''
    if len(str) < 30:
        return str
    return str[:30]+"..."

