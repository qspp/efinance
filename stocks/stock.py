import efinance as ef
import os
from datetime import date



path=r'F:\Documents\Git\efinance\stocks\\'
# 股票代码
stock_code = '688356'
# stock_code = '键凯科技'
# 数据间隔时间为 1 分钟
freq = 1
today = date.today()
# 获取最新一个交易日的分钟级别股票行情数据
df = ef.stock.get_quote_history(stock_code, klt=freq)
# 将数据存储到 csv 文件中
df.to_csv(os.path.join(path,stock_code,f'{stock_code}_{today}.csv'), encoding='utf-8-sig', index=None)

print(f'股票: {stock_code} 的行情数据已存储到文件: {stock_code}_{today}.csv 中！')
