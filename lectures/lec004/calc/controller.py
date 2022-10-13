import methodSum as sum
import methodMult as mult
import methodSub as sub
import view

def botton_click_sum():
    value_a=view.get_value()
    value_b=view.get_value()
    sum.init(value_a,value_b)
    result=sum.sum()
    view.view_data(result,'sum')

def botton_click_mult():
    value_a=view.get_value()
    value_b=view.get_value()
    mult.init(value_a,value_b)
    result=mult.sum()
    view.view_data(result,'mult')

def botton_click_sub():
    value_a=view.get_value()
    value_b=view.get_value()
    sub.init(value_a,value_b)
    result=sub.sum()
    view.view_data(result,'sub')