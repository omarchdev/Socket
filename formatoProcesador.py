import json
from datetime import datetime
from model.ResultDescomposicion import ResultDescomposicion

def convertir_a_datetime(cadena):
    formato = "%Y%m%d%H%M%S"
    fecha = datetime.strptime(cadena, formato)
    return fecha



def read_markers(marker=[]):
    array_result:list[ResultDescomposicion]=[]
    for item in marker:
        temp_item=item[1]
        data_item=  item_marker_read(temp_item)
        if(data_item!=None):
            array_result.append(ResultDescomposicion(int(item[0]), data_item,item[2],data_item["unique_id"]))   
        else:
            array_result.append(ResultDescomposicion(int(item[0]), None,"","")) 
    return array_result  
        




def item_marker_read(item=""):
    
    type_marker=""
    permite = True
    if(item.startswith("+ACK:")):
        permite=False
        type_marker="ACK"
        item=item.replace("+ACK:","")
    if(item.startswith("+RESP:")):
        type_marker="RESP"        
        item= item.replace("+RESP:","")
    if(item.startswith("+BUFF:")):
        type_marker="BUFF"
        item=item.replace("+BUFF:","")  
    if permite:
        return read_type_report(item,type_marker)
    else:
        return None
    





def read_type_report(item="",type_report=""):
    type_report = item[:5]
    data_array=item.split(",") 
    if(type_report in ["GTTOW","GTDIS","GTIOB","GTSPD","GTSOS","GTRTL","GTPNL","GTDOG","GTIGL","GTHBM","GTFRI"]):
       try:
        return  position_report_format(data_array,type_report)
       except:
           return None
    
    return None
    
    
def position_report_format(data_array:list[str],type_report:str):
    report_json=""
    if(type_report in ["GTTOW","GTDIS","GTIOB","GTSPD","GTSOS","GTRTL","GTPNL","GTDOG","GTIGL","GTHBM"]):
        
        if data_array[11]!="":
            json_data = {
                "type_report":data_array[0], 
                "protocol_version":data_array[1],
                "unique_id":data_array[2],  
                "device_name":data_array[3],    
                "reserved":data_array[4],
                "report_id":data_array[5],
                "number":data_array[6],
                "gps_accuracy":data_array[7],
                "speed":data_array[8],  
                "azimuth":data_array[9],
                "altitude":data_array[10],  
                "longitude":data_array[11],
                "latitude":data_array[12],
                "gps_utc_time":data_array[13],  
    
                "send_time":data_array[data_array.__len__()-2],
                "count_number":data_array[data_array.__len__()-1]      
            }
            return json_data
        else:
            return None
    elif(type_report == "GTFRI"):
        
        
        if data_array[11]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],
                "external_power_vcc":data_array[4],
                "report_id":data_array[5],
                "number":data_array[6], 
                "gps_accuracy":data_array[7],   
                "speed":data_array[8],
                "azimuth":data_array[9],
                "altitude":float(data_array[10]),
                "longitude":float( data_array[11]),
                "latitude":float(data_array[12]),
                "gps_utc_time":data_array[13],
                "send_time":data_array[data_array.__len__()-2],
                "count_number":data_array[data_array.__len__()-1],          
            }
            return json_data
        else:
            return None
            
    elif(type_report == "GTSTT"):
        if data_array[9]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],
                "state":data_array[4],  
                "gps_accuracy":data_array[5],  
                "speed":data_array[6],  
                "azimuth":data_array[7],    
                "altitude":data_array[8],   
                "longitude":data_array[9],  
                "latitude":data_array[10],  
                "gps_utc_time":data_array[11],  
                "send_time":data_array[data_array.__len__()-2], 
                "count_number":data_array[data_array.__len__()-1],  
            }      
            return json_data 
        else:
            return None
    elif(type_report in ["GTMPN","GTMPF","GTBTC","GTCRA"]):
        if data_array[8]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],  
                "gps_accuracy":data_array[4], 
                "speed":data_array[5],   
                "azimuth":data_array[6],    
                "altitude":data_array[7],   
                "longitude":data_array[8],  
                "latitude":data_array[9],
                "send_time":data_array[data_array.__len__()-2], 
                "count_number":data_array[data_array.__len__()-1]         
            }

            return json_data
        else:
            return None
    elif(type_report == "GTGPJ"):
        if data_array[9]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],  
                "gps_accuracy":data_array[6],
                "speed":data_array[7],  
                "azimuth":data_array[8],
                "altitude":data_array[9],
                "longitude":data_array[10],
                "latitude":data_array[11],
                "gps_utc_time":data_array[12],
                "send_time":data_array[data_array.__len__()-2], 
                "count_number":data_array[data_array.__len__()-1],

            }        
            return json_data
        else:
            return None
    elif(type_report == "GTSTC"):
        if data_array[8]!="":
            json_data={ 
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],  
                "gps_accuracy":data_array[4],
                "speed":data_array[5],
                "azimuth":data_array[6],
                "altitude":data_array[7],
                "longitude":data_array[8],
                "latitude":data_array[9],
                "gps_utc_time":data_array[10],
                "send_time":data_array[data_array.__len__()-2],
                "count_number":data_array[data_array.__len__()-1],      
            }

            return json_data
        else:
            return None
    elif (type_report == "GTBPL"):  
        if data_array[9]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],  
                "gps_accuracy":data_array[5],
                "speed":data_array[6],
                "azimuth":data_array[7],
                "altitude":data_array[8],
                "longitude":data_array[9],
                "latitude":data_array[10],  
                "gps_utc_time":data_array[11],
                "send_time":data_array[data_array.__len__()-2],
                "count_number":data_array[data_array.__len__()-1]
                }
            return json_data
        else:
            return None
    elif (type_report == "GTANT"):
        if data_array[9]!="":
            json_data={
                "type_report":data_array[0],
                "protocol_version":data_array[1],
                "unique_id":data_array[2],
                "device_name":data_array[3],  
                "external_gps_antenna":data_array[4],   
                "gps_accuracy":data_array[5],   
                "speed":data_array[6],
                "azimuth":data_array[7],
                "altitude":data_array[8],
                "longitude":data_array[9],
                "latitude":data_array[10],
                "gps_utc_time":data_array[11],
                "send_time":data_array[data_array.__len__()-2],
                "count_number":data_array[data_array.__len__()-1]
            }        
            return json_data   
        else:
            return None 
            
            
            
            
        
        
        
 
 
 
 
 
 
 
 
 
 
'''
    elif(type_report == "GTERI"):
        json_data={
            "type_report":data_array[0],
            "protocol_version":data_array[1],
            "unique_id":data_array[2],
            "device_name":data_array[3],
            "eri_mask":data_array[4],
            "external_power_supply":data_array[5],
            "report_id":data_array[6],
            "number":data_array[7],
            "gps_accuracy":data_array[8],
            "speed":data_array[9],
            "azimuth":data_array[10],
            "altitude":data_array[11],
            "longitude":data_array[12],
            "latitude":data_array[13],
            "gps_utc_time":data_array[14],
            "mcc":data_array[15],   
            "mnc":data_array[16],
            "lac":data_array[17],
            "cell_id":data_array[18],
            "reserved":data_array[19],
            "mileage":data_array[20],
            "hour_meter_count":data_array[21],
            "analogue_input":data_array[22],
            "backup_battery_porcentage":data_array[23],
            "device_status":data_array[24],
            "reserved2":data_array[25],
            "wire_device_number":data_array[26],
            "wire_device_id":data_array[27],
        
        
            
            
            
        
        }
''' 

         
        
    
        