import json
import os
import xlwt
import pymysql
import time
#save data to excel
def dataToExcel():
    ll=0
    d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
    for seq in d:
        wb=xlwt.Workbook()
        sheet=wb.add_sheet('sheet1',cell_overwrite_ok=True)
        sheet.write(0,0,'content')
        sheet.write(0,1,'createMonth')
        sheet.write(0,2,'createTime')
        sheet.write(0,3,'commentlist')
        sheet.write(0,4,'source_name')
        sheet.write(0,5,'cmtnum')
        fl=[i for i in os.listdir('mood_detail/'+seq) if i.endswith('.json')]
        print('mood_detail/'+seq)
        k=1
        for i in fl:
            with open('mood_detail/'+seq+"/"+i,'r',encoding='utf8') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print(i)
                for s in js['msglist']:
                    ll+=1
                    m=-1
                    sheet.write(k,m+1,str(s['content']))
                    sheet.write(k,m+2,str(s['createTime']))
                    timestamp = str(s['created_time'])
                    #转换成localtime
                    time_local = time.localtime(int(timestamp))
                    #转换成新的时间格式(2016-05-05 20:28:54)
                    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
                    sheet.write(k,m+3,dt)
                    if not s['commentlist']:
                        s['commentlist']=list()
                    sheet.write(k,m+4,str([(x['name'],x['uin']) for x in list(s['commentlist'])]))
                    sheet.write(k,m+5,str(s['source_name']))
                    sheet.write(k,m+6,str(s['cmtnum']))
                    k+=1
        if not os.path.exists('mood_detail/Excel/'):
            os.mkdir('mood_detail/Excel/')
        print(ll)
        try:
            wb.save('mood_detail/Excel/'+seq+'.xls')
        except Exception:
            print("error")

dataToExcel()
