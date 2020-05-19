from mvr_plugin.celery import app
import time
from celery import shared_task
import os
import datetime
from .views import *
from celery.decorators import task
from celery.utils.log import get_task_logger

#
# @app.task
# def automation_for_booking(cindate,coutdate,id,plugin):
#     if plugin=='selenium grid':
#         inc_g_var()
#         clint='http://192.168.56.1:4444/wd/hub'
#     elif plugin=='zelenium':
#         inc_z_var()
#         clint='http://192.168.99.100:4444/wd/hub'
#     yr,month,date=cindate.split('-')
#     checkin = date+"/"+month+"/"+yr
#     yr, month, date = coutdate.split('-')
#     checkout = date + "/" + month + "/" + yr
#     current_time = datetime.datetime.now()
#     end_date = current_time.strftime("%Y-%m-%d")
#     try:
#         result=booking_run(clint,checkin,checkout)
#         update_entry(id, end_date,result, "Finished", "Succesfully completed",plugin,cindate,coutdate)
#         # print(result)
#         # return render_template('result.html',param=result)
#     except Exception as e:
#         print(e.__class__.__name__)
#         update_entry(id, end_date, "No result", "Error", e.__class__.__name__,plugin,cindate,coutdate)
#         # return f"Error occured of type {e.__class__.__name__}"
#
#     if plugin == 'selenium grid':
#         dec_g_var()
#     elif plugin == 'zelenium':
#         dec_z_var()
#
#     # no_of_pending_process=len(vars.process_list)
#     # for i in range(no_of_pending_process):
#     #     # if no_of_pending_process>0:
#     #         new_process=vars.process_list[i]
#     #         print(new_process)
#     #         myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     #         mydb = myclient["mvr_result_set"]
#     #         data = mydb.Completed_test_set
#     #         output = data.find({'_id':ObjectId(new_process)})
#     #         print(output)
#     #         for m in output:
#     #             l=m
#     #         # k=0
#     #         if(l['ota']=='booking'):
#     #             prcs=vars.delete_from_list(i)
#     #             automation_for_booking(l['cindate'],l['coutdate'],new_process,plugin)
#     #             # k=1
#
#
#

