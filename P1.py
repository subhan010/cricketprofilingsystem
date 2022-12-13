import json
from itertools import chain
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
import pymongo
from bson.json_util import dumps
from bson.json_util import loads

app = Flask(__name__)
DB_URI = "mongodb+srv://ProjectDRS:123456Ass@cluster0.rkvgd.gcp.mongodb.net/CricketProfiler?retryWrites=true&w=majority" 

app.config['MONGODB_HOST'] = DB_URI
db = MongoEngine()
db.init_app(app)
 
class Bio(db.Document):
    Jersey_number =db.IntField()
    PLAYER_NAME   = db.StringField()
    Height =db.FloatField()
    State  =db.StringField()
    Role =db.StringField()
    team=db.StringField()
    batting_style=db.StringField()
    bowling_style=db.StringField()
    Test_Matches_played =db.IntField()
    ODI_Matches_played =db.IntField()
    T20_Matches_played =db.IntField()
    def to_json(self):
        return {"Jersey_number":self.Jersey_number,
                "PLAYER_NAME": self.PLAYER_NAME,
                "State":self.State,
                "Height":self.Height,
                "Role":self.Role,
                "team":self.team,
                "batting_style":self.batting_style,
                "bowling_style":self.bowling_style,
                "Test_Matches_played":self.Test_Matches_played,
                "ODI_Matches_played":self.ODI_Matches_played ,
                "T20_Matches_played":self.T20_Matches_played ,
                }
class Batting(db.Document):
    PLAYER_NAME=db.StringField()
    
    Test_Toatal_runs   = db.IntField()
    Test_Heigest_Score =db.IntField()
    Test_Average_Score  =db.FloatField()
    Test_Strike_rate =db.FloatField()
    Test_No_of_100 =db.IntField()
    Test_No_of_50 =db.IntField()

    
    ODI_Toatal_runs   = db.IntField()
    ODI_Heigest_Score =db.IntField()
    ODI_Average_Score  =db.FloatField()
    ODI_Strike_rate =db.FloatField()
    ODI_No_of_100 =db.IntField()
    ODI_No_of_50 =db.IntField()

    
    T20_Toatal_runs   = db.IntField()
    T20_Heigest_Score =db.FloatField()
    T20_Average_Score  =db.FloatField()
    T20_Strike_rate =db.IntField()
    T20_No_of_100 =db.IntField()
    T20_No_of_50 =db.IntField()
   
    def to_json(self):
        return {"PLAYER_NAME":self.PLAYER_NAME ,
                
                "Test_Toatal_runs": self.Test_Toatal_runs,
                "Test_Heigest_Score":self.Test_Heigest_Score,
                "Test_Average_Score":self.Test_Average_Score,
                "Test_Strike_rate":self.Test_Strike_rate,
                "Test_No_of_100":self.Test_No_of_100,
                "Test_No_of_50":self.Test_No_of_50,

                
                "ODI_Toatal_runs    ": self.ODI_Toatal_runs   ,
                "ODI_Heigest_Score ":self.ODI_Heigest_Score ,
                "ODI_Average_Score  ":self.ODI_Average_Score  ,
                "ODI_Strike_rate ":self.ODI_Strike_rate ,
                "ODI_No_of_100 ":self.ODI_No_of_100 ,
                "ODI_No_of_50 ":self.ODI_No_of_50 ,

                
                "T20_Toatal_runs    ": self.T20_Toatal_runs    ,
                "T20_Heigest_Score ":self.T20_Heigest_Score ,
                "T20_Average_Score  ":self.T20_Average_Score  ,
                "T20_Strike_rate   ":self.T20_Strike_rate ,
                "T20_No_of_100 ":self.T20_No_of_100 ,
                "T20_No_of_50 ":self.T20_No_of_50 ,

                
                }

class Bowling(db.Document):
    PLAYER_NAME=db.StringField()
    
    Test_Runs_Conceded   = db.IntField()
    Test_Wickets =db.IntField()
    Test_Economy  =db.FloatField()
    Test_5wickets=db.IntField()
   
    
    ODI_Runs_Conceded   = db.IntField()
    ODI_Wickets =db.IntField()
    ODI_Economy  =db.FloatField()
    ODI_5wickets=db.IntField()

    
    T20_Runs_Conceded   = db.IntField()
    T20_Wickets =db.IntField()
    T20_Economy  =db.FloatField()
    T20_5wickets=db.IntField()



    def to_json(self):
        return {"PLAYER_NAME":self.PLAYER_NAME ,
                
                "Test_Runs_Conceded": self.Test_Runs_Conceded   ,
                "Test_Wickets":self.Test_Wickets ,
                "Test_Economy":self.Test_Economy  ,
                " Test_5wickets":self. Test_5wickets,

                
                "ODI_Runs_Conceded": self.ODI_Runs_Conceded   ,
                "ODI_Wickets":self.ODI_Wickets ,
                "ODI_Economy":self.ODI_Economy  ,
                "ODI_5wickets":self.ODI_5wickets,

                
                "T20_Runs_Conceded": self.T20_Runs_Conceded,
                "T20_Wickets":self.T20_Wickets,
                "T20_Economy":self.T20_Economy  ,
                "T20_5wickets":self.T20_5wickets,
               
                } 

###################################ADMIN_SIDE######################################################
@app.route('/', methods=['GET'])
def query_records():
    Jersey_number=request.args.get('Jersey_number')
    PLAYER_NAME=request.args.get('PLAYER_NAME')
    State=request.args.get('State')
    Height=request.args.get('Height')
    team=request.args.get('team')
    batting_style=request.args.get('batting_style')
    bowling_style=request.args.get('bowling_style')
    if bool(PLAYER_NAME)==True:

        d=Bio.objects(PLAYER_NAME=PLAYER_NAME).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not j_d:
            return jsonify({'error': 'data not found'})
        else:
       
            return j_d
    elif Jersey_number != None:
    
        d = Batting.objects().filter(Test_Toatal_runs__gt=1).aggregate(*[
   
     
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        l_c=list(d)
        j_d=dumps(l_c, indent=2)
        if not d:
            return jsonify({'error': 'data not found'})
        else:
            return j_d       
        
        c = Bio.objects(Jersey_number=Jersey_number).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        
        
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        
        
        if len(l_c)==0:
            return jsonify({'error': 'data not found jer'})
        else:
            return jsonify(j_d)
    elif bool(State)==True:
        c = Bio.objects(State=State).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        if not c:
            return jsonify({'error': 'data not found Stare'})
        else:
            return jsonify(c.to_json()) 
    elif Height!=None:
        c = Bio.objects(Height=Height).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(team)==True:
        c = Bio.objects(team=team).aggregate(*[
            
        
             
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"} ,
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(batting_style)==True:
        c = Bio.objects(batting_style=batting_style).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"} ,
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(bowling_style)==True:
        c = Bio.objects(bowling_style=bowling_style).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"} ,
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json())
    else:
        c = Bio.objects().all().aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"} ,
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
        l_c=list(c)
        j_d=dumps(l_c, indent=2)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
            return j_d
         
    

   

    
 
@app.route('/Bio', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    
    c = Bio( Jersey_number=record['Jersey_number'],PLAYER_NAME=record['PLAYER_NAME'],Height=record['Height'],State=record['State'],Role=record['Role'],team=record['team'],batting_style=record['batting_style'],bowling_style=record['bowling_style'],Test_Matches_played=record['Test_Matches_played'],ODI_Matches_played=record['ODI_Matches_played'],T20_Matches_played=record['T20_Matches_played'])
    c.save()
    return jsonify(c.to_json())

@app.route('/Batting', methods=['POST'])
def create_record1():
    record = json.loads(request.data)
    d=Bio.objects(PLAYER_NAME=record['PLAYER_NAME'])
    if not d:
        return jsonify({'error':'player not found'})
        
    else:
        c = Batting(PLAYER_NAME=record['PLAYER_NAME'],Test_Toatal_runs=record['Test_Toatal_runs'],Test_Heigest_Score=record['Test_Heigest_Score'],Test_Average_Score=record['Test_Average_Score'],Test_Strike_rate=record['Test_Strike_rate'],Test_No_of_100=record['Test_No_of_100'],Test_No_of_50=record['Test_No_of_50'],ODI_Toatal_runs=record['ODI_Toatal_runs'],ODI_Heigest_Score=record['ODI_Heigest_Score'],ODI_Average_Score=record['ODI_Average_Score'],ODI_Strike_rate=record['ODI_Strike_rate'],ODI_No_of_100=record['ODI_No_of_100'],ODI_No_of_50=record['ODI_No_of_50'],T20_Toatal_runs=record['T20_Toatal_runs'],T20_Heigest_Score=record['T20_Heigest_Score'],T20_Average_Score=record['T20_Average_Score'],T20_Strike_rate=record['T20_Strike_rate'],T20_No_of_100=record['T20_No_of_100'],T20_No_of_50=record['T20_No_of_50'])
        c.save()
        return jsonify(c.to_json())

    
@app.route('/Bowling', methods=['POST'])
def create_record2():
    record = json.loads(request.data)
    d=Bio.objects(PLAYER_NAME=record['PLAYER_NAME'])
    if not d:
        return jsonify({'error':'player not found'})
        
    else:
        c = Bowling( PLAYER_NAME=record['PLAYER_NAME'],Test_Runs_Conceded=record['Test_Runs_Conceded'],Test_Wickets=record['Test_Wickets'],Test_Economy=record['Test_Economy'],Test_5wickets=record['Test_5wickets'],ODI_Runs_Conceded=record['ODI_Runs_Conceded'], ODI_Wickets=record['ODI_Wickets'],ODI_Economy=record['ODI_Economy'],ODI_5wickets=record['ODI_5wickets'],T20_Runs_Conceded=record['T20_Runs_Conceded'],T20_Wickets=record['T20_Wickets'],T20_Economy=record['T20_Economy'],T20_5wickets=record['T20_5wickets'])
        c.save()
        return jsonify(c.to_json())
        

     
@app.route('/Bio', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    c = Bio.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        c.update(Jersey_number=record['Jersey_number'])
        c.update(State=record['State'])
        c.update(Role=record['Role'])
        c.update(team=record['team'])
        c.update(Height=record['Height'])
        c.update(batting_style=record['batting_style'])
        c.update(bowling_style=record['bowling_style'])
        return jsonify(c.to_json())
@app.route('/Batting', methods=['PUT'])
def update_record1():
    record = json.loads(request.data)
    c = Batting.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        print(record['Test_Matches_played'])
        
        c.update(Test_Toatal_runs=record['Test_Toatal_runs'])
        c.update(Test_Heigest_Score=record['Test_Heigest_Score'])
        c.update(Test_Average_Score=record['Test_Average_Score'])
        c.update(Test_Strike_rate=record['Test_Strike_rate'])
        c.update(Test_No_of_100=record['Test_No_of_100'])
        
        c.update(ODI_Toatal_runs=record['ODI_Toatal_runs'])
        c.update(ODI_Heigest_Score=record['ODI_Heigest_Score'])
        c.update(ODI_Average_Score=record['ODI_Average_Score'])
        c.update(ODI_Strike_rate=record['ODI_Strike_rate'])
        c.update(ODI_No_of_100=record['ODI_No_of_100'])
        c.update(ODI_No_of_50=record['ODI_No_of_50'])
    
        c.update(T20_Toatal_runs=record['T20_Toatal_runs'])
        c.update(T20_Heigest_Score=record['T20_Heigest_Score'])
        c.update(T20_Average_Score=record['T20_Average_Score'])
        c.update(T20_Strike_rate=record['T20_Strike_rate'])
        c.update(T20_No_of_100=record['T20_No_of_100'])
        c.update(T20_No_of_50=record['T20_No_of_50'])
        
        return jsonify(c.to_json())
@app.route('/Bowling', methods=['PUT'])
def update_record2():
    record = json.loads(request.data)
    c = Bowling.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        
        
        c.update(Test_Runs_Conceded =record['Test_Runs_Conceded '])
        c.update(Test_Wickets=record['Test_Wickets'])
        c.update(Test_Economy=record['Test_Economy'])
        c.update(Test_5wickets=record['Test_5wickets'])
        
        c.update(ODI_Runs_Conceded=record['ODI_Runs_Conceded'])
        c.update(ODI_Wickets=record['ODI_Wickets'])
        c.update(ODI_Economy =record['ODI_Economy '])
        c.update(ODI_5wickets=record['ODI_5wickets'])
        
        c.update(T20_Runs_Conceded=record['T20_Runs_Conceded'])
        c.update(T20_Wickets=record['T20_Wickets'])
        c.update(T20_Economy=record['T20_Economy'])
        c.update(T20_5wickets=record['T20_5wickets'])
        return jsonify(c.to_json())
 
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    c = Bio.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    d = Batting.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    e = Bowling.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    
    if not c:
        return jsonify({'error': 'data not  found'})
    else:
        c.delete()
        d.delete()
        e.delete()
        return jsonify(c.to_json())

#############################USER_SIDE##################################################
@app.route('/<string:numo>', methods=['GET'])
def query_recordsalli(numo):
    l=numo.split('-')
    s0=""
    s1=""
    s2=""
    num=0
    
    i=0
    while i<len(l):
        if s0=="":
            s0=l[i]
            i=i+1
            print(s0)
        elif s1=="":
            s1=l[i]
            i=i+1
            print(s1)
        elif s2=="":
            s2=l[i]
            i=i+1
            print(s2)
        elif num==0:
            num=int(l[i])
            i=i+1
            print(num)
   
    if s0=="Battingo":
        if s1=="Test":
            if s2=="ToTal_runs":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_Toatal_runs__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Toatal_runs__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 

            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_Heigest_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Heigest_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                l_c=list(c)
                j_d=dumps(l_c, indent=2)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return j_d 

            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_Average_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Average_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_Strike_rate__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Strike_rate__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_No_of_100__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_No_of_100__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Batting.objects().all().filter(Test_No_of_50__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_No_of_50__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 
        elif s1=="ODI":
            if s2=="ToTal_runs":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_Toatal_runs__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                l_c=list(c)
                j_d=dumps(l_c, indent=2)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return j_d          

            elif s3=="gt":
                c = Batting.objects().all().filter(ODI_Toatal_runs__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                l_c=list(c)
                j_d=dumps(l_c, indent=2)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return j_d 

            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_Heigest_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Heigest_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_Average_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Average_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_Strike_rate__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Strike_rate__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_No_of_100__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_No_of_100__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Batting.objects().all().filter(ODI_No_of_50__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_No_of_50__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
        if s1=="T20":
            if s2=="ToTal_runs":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_Toatal_runs__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Toatal_runs__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d

            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_Heigest_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Heigest_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d

            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_Average_Score__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Average_Score__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_Strike_rate__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Strike_rate__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_No_of_100__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_No_of_100__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Batting.objects().all().filter(T20_No_of_50__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_No_of_50__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 
    
    elif s0=="Bowlingo":
        if s1=="test":
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Bowling.objects().all().filter(Test_Runs_Conceded__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio_STATICTIS"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not j_d:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Runs_Conceded__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"},
                   { 
          '$lookup': {
              'from': Bowling._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BOWLING_STATICTIS'}
              
         },
          {'$unwind': "$BOWLING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d 

            elif s2=="wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(Test_Wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="economy":
                if s3=="lt":
                    c = Bowling.objects().all().filter(Test_Economy__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_Economy__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="5wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(Test_5wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(Test_5wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            
        elif s1=="odi":
            
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Bowling.objects().all().filter(ODI_Runs_Conceded__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Runs_Conceded__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(ODI_Wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    _c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="economy":
                if s3=="lt":
                    c = Bowling.objects().all().filter(ODI_Economy__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_Economy__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="5wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(ODI_5wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(ODI_5wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
        elif s1=="t20":
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Bowling.objects().all().filter(T20_Runs_Conceded__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Runs_Conceded__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(T20_Wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="economy":
                if s3=="lt":
                    c = Bowling.objects().all().filter(T20_Economy__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_Economy__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
            elif s2=="5wickets":
                if s3=="lt":
                    c = Bowling.objects().all().filter(T20_5wickets__lt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d          

                elif s3=="gt":
                    c = Batting.objects().all().filter(T20_5wickets__gt=num).aggregate(*[
            
        
            
         { 
          '$lookup': {
              'from': Bio._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'Bio'}
              
         },
          {'$unwind': "$Bio"},
                   { 
          '$lookup': {
              'from': Batting._get_collection_name(),
              'localField': 'PLAYER_NAME',
              'foreignField': 'PLAYER_NAME',
              'as': 'BATTING_STATICTIS'}
              
         },
          {'$unwind': "$BATTING_STATICTIS"}
     
         ])
                    l_c=list(c)
                    j_d=dumps(l_c, indent=2)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return j_d
                



if __name__ == "__main__":
    app.run(debug=True)
