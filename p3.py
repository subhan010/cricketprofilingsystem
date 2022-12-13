import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine


app = Flask(__name__)
DB_URI = "mongodb+srv://ProjectDRS:123456Ass@cluster0.rkvgd.gcp.mongodb.net/CricketProfiler?retryWrites=true&w=majority" 

app.config['MONGODB_HOST'] = DB_URI
db = MongoEngine()
db.init_app(app)
 
class Profile(db.Document):
    Jersey_number =db.IntField()
    PLAYER_NAME  = db.StringField()
    Height=db.FloatField()
    State =db.StringField()
    Role=db.StringField()
    team=db.StringField()
    batting_style=db.StringField()
    bowling_style=db.StringField()
    Test_Matches_played =db.IntField()
    ODI_Matches_played =db.IntField()
    T20_Matches_played =db.IntField()
    
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
                "Test_Toatal_runs": self.Test_Toatal_runs,
                "Test_Heigest_Score":self.Test_Heigest_Score,
                "Test_Average_Score":self.Test_Average_Score,
                "Test_Strike_rate":self.Test_Strike_rate,
                "Test_No_of_100":self.Test_No_of_100,
                "Test_No_of_50":self.Test_No_of_50,
                "ODI_Toatal_runs": self.ODI_Toatal_runs,
                "ODI_Heigest_Score":self.ODI_Heigest_Score,
                "ODI_Average_Score":self.ODI_Average_Score,
                "ODI_Strike_rate":self.ODI_Strike_rate,
                "ODI_No_of_100":self.ODI_No_of_100,
                "ODI_No_of_50":self.ODI_No_of_50,

                
                "T20_Toatal_runs": self.T20_Toatal_runs,
                "T20_Heigest_Score":self.T20_Heigest_Score,
                "T20_Average_Score":self.T20_Average_Score,
                "T20_Strike_rate":self.T20_Strike_rate,
                "T20_No_of_100":self.T20_No_of_100,
                "T20_No_of_50":self.T20_No_of_50,

                "Test_Runs_Conceded": self.Test_Runs_Conceded,
                "Test_Wickets":self.Test_Wickets,
                "Test_Economy":self.Test_Economy,
                "Test_5wickets":self.Test_5wickets,

                
                "ODI_Runs_Conceded": self.ODI_Runs_Conceded,
                "ODI_Wickets":self.ODI_Wickets,
                "ODI_Economy":self.ODI_Economy,
                "ODI_5wickets":self.ODI_5wickets,

                
                "T20_Runs_Conceded": self.T20_Runs_Conceded,
                "T20_Wickets":self.T20_Wickets,
                "T20_Economy":self.T20_Economy,
                "T20_5wickets":self.T20_5wickets
                }
  

###################################ADMIN_SIDE######################################################
@app.route('/admin', methods=['GET'])
def query_records():
    Jersey_number=request.args.get('Jersey_number')
    PLAYER_NAME=request.args.get('PLAYER_NAME')
    State=request.args.get('State')
    Height=request.args.get('Height')
    team=request.args.get('team')
    batting_style=request.args.get('batting_style')
    bowling_style=request.args.get('bowling_style')
    if bool(PLAYER_NAME)==True:

        c=Profile.objects(PLAYER_NAME=PLAYER_NAME).first()
        
        
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json())
    elif Jersey_number != None:
    
        
        
        c = Profile.objects(Jersey_number=Jersey_number).first()
        if not  c:
            return jsonify({'error': 'data not found '})
        else:
            return jsonify(c.to_json())
    elif bool(State)==True:
        c = Profile.objects(State=State).first()
        if not c:
            return jsonify({'error': 'data not found '})
        else:
            return jsonify(c.to_json()) 
    elif Height!=None:
        c = Profile.objects(Height=Height).first()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(team)==True:
        c = Profile.objects(team=team).first()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(batting_style)==True:
        c = Profile.objects(batting_style=batting_style).first()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(bowling_style)==True:
        c = Profile.objects(bowling_style=bowling_style).first()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json())
    else:
        c = Profile.objects().all()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(c.to_json())
         
    

   

    
 
@app.route('/admin', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    
    c = Profile( Jersey_number=record['Jersey_number'],PLAYER_NAME=record['PLAYER_NAME'],Height=record['Height'],State=record['State'],Role=record['Role'],team=record['team'],batting_style=record['batting_style'],bowling_style=record['bowling_style'],Test_Matches_played=record['Test_Matches_played'],ODI_Matches_played=record['ODI_Matches_played'],T20_Matches_played=record['T20_Matches_played'],Test_Toatal_runs=record['Test_Toatal_runs'],Test_Heigest_Score=record['Test_Heigest_Score'],Test_Average_Score=record['Test_Average_Score'],Test_Strike_rate=record['Test_Strike_rate'],Test_No_of_100=record['Test_No_of_100'],Test_No_of_50=record['Test_No_of_50'],ODI_Toatal_runs=record['ODI_Toatal_runs'],ODI_Heigest_Score=record['ODI_Heigest_Score'],ODI_Average_Score=record['ODI_Average_Score'],ODI_Strike_rate=record['ODI_Strike_rate'],ODI_No_of_100=record['ODI_No_of_100'],ODI_No_of_50=record['ODI_No_of_50'],T20_Toatal_runs=record['T20_Toatal_runs'],T20_Heigest_Score=record['T20_Heigest_Score'],T20_Average_Score=record['T20_Average_Score'],T20_Strike_rate=record['T20_Strike_rate'],T20_No_of_100=record['T20_No_of_100'],T20_No_of_50=record['T20_No_of_50'],Test_Runs_Conceded=record['Test_Runs_Conceded'],Test_Wickets=record['Test_Wickets'],Test_Economy=record['Test_Economy'],Test_5wickets=record['Test_5wickets'],ODI_Runs_Conceded=record['ODI_Runs_Conceded'], ODI_Wickets=record['ODI_Wickets'],ODI_Economy=record['ODI_Economy'],ODI_5wickets=record['ODI_5wickets'],T20_Runs_Conceded=record['T20_Runs_Conceded'],T20_Wickets=record['T20_Wickets'],T20_Economy=record['T20_Economy'],T20_5wickets=record['T20_5wickets'])
    c.save()
    return jsonify(c.to_json())


        

     
@app.route('/admin', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    print(record)
    c = Profile.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        if 'Jersey_number' in record:
            c.update(Jersey_number=record['Jersey_number'])
        if 'State' in record:
            c.update(State=record['State'])
        if 'Role' in record:
            c.update(Role=record['Role'])
        if 'team' in record:
            c.update(team=record['team'])
        if 'Height' in record:
            c.update(Height=record['Height'])
        if 'batting_style' in record:
            c.update(batting_style=record['batting_style'])
        if 'bowling_style' in record:
            c.update(bowling_style=record['bowling_style'])
        if 'Test_Matches_played' in record:
            c.update(Test_Matches_played=record['Test_Matches_played'])
        if 'ODI_Matches_played' in record:
            c.update(Test_Matches_played=record['ODI_Matches_played'])
        if 'T20_Matches_played' in record:
            c.update(Test_Matches_played=record['T20_Matches_played'])
        
        if 'Test_Toatal_runs' in record:
            c.update(Test_Toatal_runs=record['Test_Toatal_runs'])
        if 'Test_Heigest_Score' in record:
            c.update(Test_Heigest_Score=record['Test_Heigest_Score'])
        if 'Test_Average_Score' in record:
            c.update(Test_Average_Score=record['Test_Average_Score'])
        if 'Test_Strike_rate' in record:
            c.update(Test_Strike_rate=record['Test_Strike_rate'])
        if 'Test_No_of_100' in record:
            c.update(Test_No_of_100=record['Test_No_of_100'])
        if 'ODI_Toatal_runs' in record:
        
            c.update(ODI_Toatal_runs=record['ODI_Toatal_runs'])
        if 'ODI_Heigest_Score' in record:
            c.update(ODI_Heigest_Score=record['ODI_Heigest_Score'])
        if 'ODI_Average_Score' in record:
            c.update(ODI_Average_Score=record['ODI_Average_Score'])
        if 'ODI_Strike_rate' in record:
            c.update(ODI_Strike_rate=record['ODI_Strike_rate'])
        if 'ODI_No_of_100' in record:
            c.update(ODI_No_of_100=record['ODI_No_of_100'])
        if 'ODI_No_of_50' in record:
            c.update(ODI_No_of_50=record['ODI_No_of_50'])
        if 'T20_Toatal_runs' in record:
    
            c.update(T20_Toatal_runs=record['T20_Toatal_runs'])
        if 'T20_Heigest_Score' in record:
            c.update(T20_Heigest_Score=record['T20_Heigest_Score'])
        if 'T20_Average_Score' in record:
            c.update(T20_Average_Score=record['T20_Average_Score'])
        if 'T20_Strike_rate' in record:
            c.update(T20_Strike_rate=record['T20_Strike_rate'])
        if 'T20_No_of_100' in record:
            c.update(T20_No_of_100=record['T20_No_of_100'])
        if 'T20_No_of_50' in record:
            c.update(T20_No_of_50=record['T20_No_of_50'])
        if 'Test_Runs_Conceded' in record:

            c.update(Test_Runs_Conceded =record['Test_Runs_Conceded '])
        if 'Test_Wickets' in record:
            c.update(Test_Wickets=record['Test_Wickets'])
        if 'Test_Economy' in record:
            c.update(Test_Economy=record['Test_Economy'])
        if 'Test_5wickets' in record:
            c.update(Test_5wickets=record['Test_5wickets'])
        if 'ODI_Runs_Conceded' in record:
            c.update(ODI_Runs_Conceded=record['ODI_Runs_Conceded'])
        if 'ODI_Wickets' in record:
            c.update(ODI_Wickets=record['ODI_Wickets'])
        if 'ODI_Economy' in record:
            c.update(ODI_Economy =record['ODI_Economy '])
        if 'ODI_5wickets' in record:
            c.update(ODI_5wickets=record['ODI_5wickets'])
        if 'T20_Runs_Conceded' in record:
            c.update(T20_Runs_Conceded=record['T20_Runs_Conceded'])
        if 'T20_Wickets' in record:
            c.update(T20_Wickets=record['T20_Wickets'])
        if 'T20_Economy' in record:
            c.update(T20_Economy=record['T20_Economy'])
        if 'T20_5wickets' in record:
            c.update(T20_5wickets=record['T20_5wickets'])
        return jsonify(c.to_json())

 
@app.route('/admin', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    c = Profile.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
   
    
    if not c:
        return jsonify({'error': 'data not  found'})
    else:
        c.delete()
        return jsonify(c.to_json())

#############################USER_SIDE##################################################
@app.route('/<string:numo>', methods=['GET'])
def query_recordsalli(numo):
    print(numo)
    l=numo.split('-')

    s0=""
    s1=""
    s2=""
    s3=""
    num=0
    print(l)
    i=0
    while i<len(l):
        if s0=="":
            s0=l[i]
            i=i+1
            
        elif s1=="":
            s1=l[i]
            i=i+1
            
        elif s2=="":
            s2=l[i]
            i=i+1
            
            print(s2)
        elif s3=="":
            s3=l[i]
            i=i+1
            
        elif num==0:
            num=int(l[i])
            i=i+1
            
  
   
    if s0=="Batting":
        if s1=="Test":
            if s2=="Total_runs":
                if s3=="lt":
                    c = Profile.objects().filter(Test_Toatal_runs__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return  jsonify(c.to_json())         

                elif s3=="gt":
                    c = Profile.objects().filter(Test_Toatal_runs__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 
            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Heigest_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Heigest_Score__gt=num)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json()) 

            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Average_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Average_Score__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Strike_rate__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Strike_rate__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_No_of_100__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_No_of_100__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_No_of_50__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_No_of_50__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 
        elif s1=="ODI":
            if s2=="Total_runs":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Toatal_runs__lt=num)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())          

            elif s3=="gt":
                c = Profile.objects().all().filter(ODI_Toatal_runs__gt=num)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json()) 

            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Heigest_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Heigest_Score__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Average_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Average_Score__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Strike_rate__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Strike_rate__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_No_of_100__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_No_of_100__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_No_of_50__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_No_of_50__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
        if s1=="T20":
            if s2=="Total_runs":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Toatal_runs__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Toatal_runs__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())

            elif s2=="Heigest_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Heigest_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Heigest_Score__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())

            
            elif s2=="Average_Score":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Average_Score__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Average_Score__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())

            elif s2=="Strike_rate":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Strike_rate__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Strike_rate__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())

        
            elif s2=="No_of_100":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_No_of_100__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_No_of_100__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            

            elif s2=="No_of_50":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_No_of_50__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_No_of_50__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 
    
    elif s0=="Bowling":
        if s1=="test":
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Runs_Conceded__lt=num)
                    if not jsonify(c.to_json()):
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Runs_Conceded__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json()) 

            elif s2=="wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="economy":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_Economy__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_Economy__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="5wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(Test_5wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(Test_5wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            
        elif s1=="odi":
            
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Runs_Conceded__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Runs_Conceded__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="economy":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_Economy__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_Economy__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="5wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(ODI_5wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(ODI_5wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
        elif s1=="t20":
            if s2=="Runs_conceded":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Runs_Conceded__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Runs_Conceded__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="economy":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_Economy__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_Economy__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
            elif s2=="5wickets":
                if s3=="lt":
                    c = Profile.objects().all().filter(T20_5wickets__lt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())          

                elif s3=="gt":
                    c = Profile.objects().all().filter(T20_5wickets__gt=num)
                    if not c:
                        return jsonify({'error': 'data not found'})
                    else:
                        return jsonify(c.to_json())
                
    elif s0=="Bio":
        if s1=="Jersey_number":
            c=Profile.objects(Jersey_number=int(s2)).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="Height":
            if s2=="lt":
                c=Profile.objects().all().filter(Height__lt=int(s3))
                if not c:
                        return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())
        
            if s2=="gt":
                c=Profile.objects().all().filter(Height__gt=int(s3))
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())


        elif s1=="State":
            c=Profile.objects(State=s2).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="Role":
            c=Profile.objects(Role=s2).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="team":
            c=Profile.objects(team=s2).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="batting_style":
            c=Profile.objects(batting_style=s2).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="bowling_style":
            c=Profile.objects(bowling_style=s2).all()
            if not c:
                return jsonify({'error': 'data not found'})
            else:
                return jsonify(c.to_json())

        elif s1=="Test_Matches_played":
            if s2=="lt":
                c=Profile.objects().all().filter(Test_Matches_played__lt=int(s3))
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())
        
            if s2=="gt":
                c=Profile.objects().all().filter(Test_Matches_played__gt=int(s3))
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())

        elif s1=="ODI_Matches_played":
            if s2=="lt":
                c=Profile.objects().all().filter(ODI_Matches_played__lt=(s3))
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())
                       
        
            if s2=="gt":
                c=Profile.objects().all().filter(ODI_Matches_played__gt=s3)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())

        elif s1=="T20_Matches_played":
            if s2=="lt":
                c=Profile.objects().all().filter(T20_Matches_played__lt=s3)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())
        
            if s2=="gt":
                c=Profile.objects().all().filter(T20_Matches_played__gt=s3)
                if not c:
                    return jsonify({'error': 'data not found'})
                else:
                    return jsonify(c.to_json())



if __name__ == "__main__":
    app.run(debug=True)
