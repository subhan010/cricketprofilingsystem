import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
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
    Test_Toatal_runs   = db.IntField()
    Test_Heigest_Score =db.IntField()
    Test_Average_Score  =db.FloatField()
    Test_Strike_rate =db.FloatField()
    Test_No_of_100 =db.db.IntField()
    Test_No_of_50 =db.db.IntField()

    ODI_Matches_played =db.IntField()
    ODI_Toatal_runs   = db.IntField()
    ODI_Heigest_Score =db.IntField()
    ODI_Average_Score  =db.FloatField()
    ODI_Strike_rate =db.FloatField()
    ODI_No_of_100 =db.IntField()
    ODI_No_of_50 =db.IntField()

    T20_Matches_played =db.IntField()
    T20_Toatal_runs   = db.IntField()
    T20_Heigest_Score =db.FloatField()
    T20_Average_Score  =db.FloatField()
    T20_Strike_rate =db.IntField()
    T20_No_of_100 =db.IntField()
    T20_No_of_50 =db.IntField()
    def to_json(self):
        return {"Jersey_number":self.Jersey_number,
                "PLAYER_NAME": self.PLAYER_NAME,
                "State":self.State,
                "Height":self.Height,
                "Role":self.Role,
                "team":self.team,
                "batting_style":self.batting_style,
                "bowling_style":self.bowling_style
                }
class Batting(db.Document):
    
   
    def to_json(self):
        return {"Test_Matches_played":self.Test_Matches_played,
                "Test_Toatal_runs": self.Test_Toatal_runs,
                "Test_Heigest_Score":self.Test_Heigest_Score,
                "Test_Average_Score":self.Test_Average_Score,
                "Test_Strike_rate":self.Test_Strike_rate,
                "Test_No_of_100":self.Test_No_of_100,
                "Test_No_of_50":self.Test_No_of_50,

                "ODI_Matches_played ":self.ODI_Matches_played ,
                "ODI_Toatal_runs    ": self.ODI_Toatal_runs   ,
                "ODI_Heigest_Score ":self.ODI_Heigest_Score ,
                "ODI_Average_Score  ":self.ODI_Average_Score  ,
                "ODI_Strike_rate ":self.ODI_Strike_rate ,
                "ODI_No_of_100 ":self.ODI_No_of_100 ,
                "ODI_No_of_50 ":self.ODI_No_of_50 ,

                "T20_Matches_played ":self.T20_Matches_played ,
                "T20_Toatal_runs    ": self.T20_Toatal_runs    ,
                "T20_Heigest_Score ":self.T20_Heigest_Score ,
                "T20_Average_Score  ":self.T20_Average_Score  ,
                "T20_Strike_rate   ":self.T20_Strike_rate ,
                "T20_No_of_100 ":self.T20_No_of_100 ,
                "T20_No_of_50 ":self.T20_No_of_50 ,

                
                }

class Bowling(db.Document):
    
    PLAYER_NAME=db.IntField()
    Test_Matches =db.IntField()
    Test_Runs_Conceded   = db.IntField()
    Test_Wickets =db.IntField()
    Test_Economy  =db.FloatField()
    Test_5wickets=db.IntField()
   
    ODI_Matches =db.IntField()
    ODI_Runs_Conceded   = db.IntField()
    ODI_Wickets =db.IntField()
    ODI_Economy  =db.FloatField()
    ODI_5wickets=db.IntField()

    T20_Matches =db.IntField()
    T20_Runs_Conceded   = db.IntField()
    T20_Wickets =db.IntField()
    T20_Economy  =db.FloatField()
    T20_5wickets=db.IntField()



    def to_json(self):
        return {"Test_Matches ":self.Test_Matches ,
                "Test_Runs_Conceded   ": self.Test_Runs_Conceded   ,
                "Test_Wickets ":self.Test_Wickets ,
                "Test_Economy  ":self.Test_Economy  ,
                " Test_5wickets":self. Test_5wickets,

                "ODI_Matches ":self.ODI_Matches ,
                "ODI_Runs_Conceded   ": self.ODI_Runs_Conceded   ,
                "ODI_Wickets ":self.ODI_Wickets ,
                "ODI_Economy  ":self.ODI_Economy  ,
                "ODI_5wickets":self.ODI_5wickets,

                "T20_Matches ":self.T20_Matches ,
                "T20_Runs_Conceded": self.PLAYER_NAME,
                "T20_Wickets":self.State,
                "T20_Economy  ":self.T20_Economy  ,
                "T20_5wickets":self.T20_5wickets,
               
                } 


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
        c = Bio.objects(PLAYER_NAME=PLAYER_NAME)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json())
    elif Jersey_number != None:
        print(Jersey_number)
        c = Bio.objects(Jersey_number=Jersey_number) 
        if not c:
            return jsonify({'error': 'data not found jer'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(State)==True:
        c = Bio.objects(State=State)
        
        if not c:
            return jsonify({'error': 'data not found Stare'})
        else:
       
            return jsonify(c.to_json()) 
    elif Height!=None:
        c = Bio.objects(Height=Height)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(team)==True:
        c = Bio.objects(team=team)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(batting_style)==True:
        c = Bio.objects(batting_style=batting_style)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json()) 
    elif bool(bowling_style)==True:
        c = Bio.objects(bowling_style=bowling_style)
        if not c:
            return jsonify({'error': 'data not found'})
        else:
       
            return jsonify(c.to_json())
    else:
        c = Bio.objects().all()
        if not c:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(c.to_json())
         
    

   
@app.route('/all', methods=['GET'])
def query_recordsall():

    c = Bio.objects().all()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(c.to_json())
    
 
@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    c = Bio( Jersey_number=record['Jersey_number'],PLAYER_NAME=record['PLAYER_NAME'],Height=record['Height'],State=record['State'],Role=record['Role'],team=record['team'],batting_style=record['batting_style'],bowling_style=record['bowling_style'])
    c.save()
    return jsonify(c.to_json())
 
@app.route('/', methods=['PUT'])
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
 
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    c = Bio.objects(PLAYER_NAME=record['PLAYER_NAME']).first()
    if not c:
        return jsonify({'error': 'data not  found'})
    else:
        c.delete()
        return jsonify(c.to_json())
#############################################################################




if __name__ == "__main__":
    app.run(debug=True)
