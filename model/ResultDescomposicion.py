
class ResultDescomposicion:
    id=0
    json_data:dict[str,str]
    fecha_captura=""
    unique_id_vehicle=""
    def __init__(self,id,json_data,fecha_captura,unique_id_vehicle):
        self.id=id
        self.json_data=json_data
        self.fecha_captura=fecha_captura
        self.unique_id_vehicle=unique_id_vehicle
    
