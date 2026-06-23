#!/usr/bin/env python3
import json
O=r"C:\Users\agnes\Desktop\projects\turkish-code-instructions\submissions\security_refactor_extra.json"
D=[]
def S(i,r,l):
    D.append({"instruction":"Bu kodda guvenlik acigi var mi? Coz:\n"+i,"response":r,"language":l,"category":"security","type":"manual","format":"security"})
def R(i,r,l):
    D.append({"instruction":"Bu kodu iyilestir:\n"+i,"response":r,"language":l,"category":"refactoring","type":"manual","format":"refactoring"})
def b(l,bad,good):
    return (f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```")

# ===== SECURITY =====
pairs_sec = [
    # SQL Injection
    ("python","def get(u):\n    c=sqlite3.connect('d.db')\n    q=f\"SELECT * FROM users WHERE id={u}\"\n    return c.execute(q).fetchone()","def get(u):\n    c=sqlite3.connect('d.db')\n    c.execute(\"SELECT * FROM users WHERE id=?\",(u,))\n    return c.fetchone()"),
    ("python","def search(n):\n    cur.execute(\"SELECT * FROM products WHERE name LIKE '%\"+n+\"%'\")","def search(n):\n    cur.execute(\"SELECT * FROM products WHERE name LIKE ?\",('%'+n+'%',))"),
    ("python","def login(u,p):\n    cur.execute(\"SELECT id FROM users WHERE username='\"+u+\"' AND pass='\"+p+\"'\")","def login(u,p):\n    cur.execute(\"SELECT id FROM users WHERE username=? AND password=?\",(u,p))"),
    ("python","def upd(uid,e):\n    db.execute(\"UPDATE users SET email='\"+e+\"' WHERE id=\"+str(uid))","def upd(uid,e):\n    db.execute(\"UPDATE users SET email=? WHERE id=?\",(e,uid))"),
    ("python","def delr(uid):\n    db.execute(\"DELETE FROM users WHERE id=\"+uid)","def delr(uid):\n    db.execute(\"DELETE FROM users WHERE id=?\",(uid,))"),
    ("python","def get_orders(dr):\n    q=f\"SELECT * FROM orders WHERE date BETWEEN '{dr[0]}' AND '{dr[1]}'\"\n    return db.execute(q)","def get_orders(dr):\n    q=\"SELECT * FROM orders WHERE date BETWEEN ? AND ?\"\n    return db.execute(q,(dr[0],dr[1]))"),
    ("javascript","app.get('/user',(r,s)=>{const q=`SELECT * FROM users WHERE id=${r.query.id}`;db.query(q,(e,ro)=>s.json(ro))})","app.get('/user',(r,s)=>{db.query('SELECT * FROM users WHERE id=?',[r.query.id],(e,ro)=>s.json(ro))})"),
    ("javascript","connection.query(\"SELECT * FROM products WHERE name='\"+req.body.n+\"'\",(e,ro)=>res.send(ro))","connection.query(\"SELECT * FROM products WHERE name=?\",[req.body.n],(e,ro)=>res.send(ro))"),
    ("javascript","app.post('/login',(r,s)=>{const{u,p}=r.body;db.query(`SELECT id FROM users WHERE username='${u}' AND pass='${p}'`,(e,ro)=>{if(ro.length)s.json({ok:1});else s.status(401).json({ok:0})})})","app.post('/login',(r,s)=>{db.query('SELECT id FROM users WHERE username=? AND pass=?',[r.body.u,r.body.p],(e,ro)=>{if(ro.length)s.json({ok:1});else s.status(401).json({ok:0})})})"),
    ("javascript","app.get('/search',(r,s)=>{db.execute(`SELECT * FROM articles WHERE title LIKE '%${r.query.q}%'`,(e,ro)=>s.render('s',{r:ro}))})","app.get('/search',(r,s)=>{db.execute('SELECT * FROM articles WHERE title LIKE ?',['%'+r.query.q+'%'],(e,ro)=>s.render('s',{r:ro}))})"),
    ("javascript","app.delete('/user',(r,s)=>{db.query(\"DELETE FROM users WHERE id=\"+r.body.id,(e)=>s.send('ok'))})","app.delete('/user',(r,s)=>{db.query(\"DELETE FROM users WHERE id=?\",[r.body.id],(e)=>s.send('ok'))})"),
    ("java","User get(String id)throws SQLException{ResultSet rs=conn.createStatement().executeQuery(\"SELECT * FROM users WHERE id=\"+id);return mapUser(rs)}","User get(String id)throws SQLException{PreparedStatement ps=conn.prepareStatement(\"SELECT * FROM users WHERE id=?\");ps.setString(1,id);return mapUser(ps.executeQuery())}"),
    ("java","List<Product>search(String n)throws SQLException{String s=\"SELECT * FROM products WHERE name LIKE '%\"+n+\"%'\";Statement st=db.createStatement();return mapProducts(st.executeQuery(s))}","List<Product>search(String n)throws SQLException{PreparedStatement ps=db.prepareStatement(\"SELECT * FROM products WHERE name LIKE ?\");ps.setString(1,\"%\"+n+\"%\");return mapProducts(ps.executeQuery())}"),
    ("java","boolean login(String u,String p)throws SQLException{ResultSet rs=conn.createStatement().executeQuery(\"SELECT id FROM users WHERE username='\"+u+\"' AND password='\"+p+\"'\");return rs.next()}","boolean login(String u,String p)throws SQLException{PreparedStatement ps=conn.prepareStatement(\"SELECT id FROM users WHERE username=? AND password=?\");ps.setString(1,u);ps.setString(2,p);return ps.executeQuery().next()}"),
    ("java","void upd(int uid,String e)throws SQLException{conn.createStatement().executeUpdate(\"UPDATE users SET email='\"+e+\"' WHERE id=\"+uid)}","void upd(int uid,String e)throws SQLException{PreparedStatement ps=conn.prepareStatement(\"UPDATE users SET email=? WHERE id=?\");ps.setString(1,e);ps.setInt(2,uid);ps.executeUpdate()}"),
    ("go","func Get(db *sql.DB,id string)(*User,error){row:=db.QueryRow(fmt.Sprintf(\"SELECT * FROM users WHERE id='%s'\",id));var u User;err:=row.Scan(&u.ID,&u.Name);return &u,err}","func Get(db *sql.DB,id string)(*User,error){row:=db.QueryRow(\"SELECT * FROM users WHERE id=?\",id);var u User;err:=row.Scan(&u.ID,&u.Name);return &u,err}"),
    ("go","func Search(db *sql.DB,n string)([]Product,error){rows,err:=db.Query(fmt.Sprintf(\"SELECT * FROM products WHERE name LIKE '%%%s%%'\",n));return mapProducts(rows),err}","func Search(db *sql.DB,n string)([]Product,error){rows,err:=db.Query(\"SELECT * FROM products WHERE name LIKE ?\",\"%\"+n+\"%\");return mapProducts(rows),err}"),
    ("go","func Login(db *sql.DB,u,p string)bool{row:=db.QueryRow(\"SELECT id FROM users WHERE username='\"+u+\"' AND password='\"+p+\"'\");var id int;return row.Scan(&id)==nil}","func Login(db *sql.DB,u,p string)bool{row:=db.QueryRow(\"SELECT id FROM users WHERE username=? AND password=?\",u,p);var id int;return row.Scan(&id)==nil}"),
    ("web","<?php $id=$_GET['id'];$r=mysqli_query($c,\"SELECT * FROM users WHERE id=$id\");?>","<?php $stmt=$c->prepare(\"SELECT * FROM users WHERE id=?\");$stmt->bind_param(\"i\",$id);$id=$_GET['id'];$stmt->execute();$r=$stmt->get_result();?>"),
    ("web","<?php $u=$_POST['u'];$p=$_POST['p'];$r=$db->query(\"SELECT id FROM admins WHERE user='$u' AND pass='$p'\");?>","<?php $stmt=$db->prepare(\"SELECT id FROM admins WHERE user=? AND pass=?\");$stmt->execute([$_POST['u'],$_POST['p']]);$r=$stmt->get_result();?>"),
    # XSS
    ("python","@app.route('/s')\\ndef s():\\n    q=request.args.get('q','')\\n    return f'<div>{q}</div>'","from markupsafe import escape\\n@app.route('/s')\\ndef s():\\n    return f'<div>{escape(request.args.get(\"q\",\"\"))}</div>'"),
    ("python","def dis(c):return '<div>'+c+'</div>'","from html import escape\\ndef dis(c):return '<div>'+escape(c)+'</div>'"),
    ("python","def show(u):return Template('<h1>$n</h1>').substitute(n=u['n'])","from markupsafe import escape\\ndef show(u):return Template('<h1>$n</h1>').substitute(n=escape(u['n']))"),
    ("python","@app.route('/h')\\ndef h():\\n    n=request.args.get('n','w')\\n    return f'<h1>Merhaba {n}</h1>'","from markupsafe import escape\\n@app.route('/h')\\ndef h():\\n    return f'<h1>Merhaba {escape(request.args.get(\"n\",\"w\"))}</h1>'"),
    ("javascript","document.getElementById('o').innerHTML='<p>'+inp+'</p>'","document.getElementById('o').textContent=inp"),
    ("javascript","$('#l').append('<li>'+u+'</li>')","$('#l').append(document.createTextNode(u))"),
    ("javascript","app.get('/p',(r,s)=>{s.send('<h1>'+r.query.n+'</h1>')})","const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');\\napp.get('/p',(r,s)=>{s.send('<h1>'+esc(r.query.n)+'</h1>')})"),
    ("javascript","function s(m){document.write('<div>'+m+'</div>')}","function s(m){const d=document.createElement('div');d.textContent=m;document.body.appendChild(d)}"),
    ("java","@GetMapping(\"/h\")@ResponseBody String h(@RequestParam String n){return \"<h1>\"+n+\"</h1>\";}","import org.springframework.web.util.HtmlUtils;\\n@GetMapping(\"/h\")@ResponseBody String h(@RequestParam String n){return \"<h1>\"+HtmlUtils.htmlEscape(n)+\"</h1>\";}"),
    ("java","String r(String c){return \"<div>\"+c+\"</div>\";}","import org.owasp.encoder.Encode;\\nString r(String c){return \"<div>\"+Encode.forHtml(c)+\"</div>\";}"),
    ("java","@GetMapping(\"/u\")String u(@RequestParam String n){return \"<p>\"+n+\"</p>\";}","import org.springframework.web.util.HtmlUtils;\\n@GetMapping(\"/u\")@ResponseBody String u(@RequestParam String n){return \"<p>\"+HtmlUtils.htmlEscape(n)+\"</p>\";}"),
    ("go","func h(w http.ResponseWriter,r*http.Request){fmt.Fprintf(w,\"<h1>%s</h1>\",r.URL.Query().Get(\"n\"))}","func h(w http.ResponseWriter,r*http.Request){n:=r.URL.Query().Get(\"n\");tmpl:=template.Must(template.New(\"t\").Parse(\"<h1>{{.}}</h1>\"));tmpl.Execute(w,n)}"),
    ("go","func s(w http.ResponseWriter,t string){w.Write([]byte(\"<div>\"+t+\"</div>\"))}","import \"html\"\\nfunc s(w http.ResponseWriter,t string){w.Write([]byte(\"<div>\"+html.EscapeString(t)+\"</div>\"))}"),
    ("web","<script>var n=URLSearchParams(location.s).get('n');document.getElementById('g').innerHTML='<h1>'+n+'</h1>';</script>","<script>var n=URLSearchParams(location.s).get('n');document.getElementById('g').textContent=n;</script>"),
    ("web","<script>var m=getParam('m');eval('alert(\"'+m+'\")');</script>","<script>var m=getParam('m');m=m.replace(/[<>&\"']/g,'');alert(m);</script>"),
    ("web","<%= raw comment.body %>","<%= h(comment.body) %>"),
]
for l,bad,good in pairs_sec:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

# ===== REFACTORING =====
pairs_ref = [
    # Python refactoring
    ("python","def calc(a,b,c,d):\\n    total=a+b+c+d\\n    return total*0.18","def calc(*args):\\n    return sum(args)*0.18"),
    ("python","if x>0 and x<100:\\n    return True\\nelse:\\n    return False","return 0<x<100"),
    ("python","items = []\\nfor i in range(10):\\n    items.append(i*2)","items = [i*2 for i in range(10)]"),
    ("python","def process(data):\\n    if data:\\n        if data.get('active'):\\n            if data['active']==True:\\n                return 'ok'\\n    return 'no'","def process(data):\\n    if not data or not data.get('active'):\\n        return 'no'\\n    return 'ok'"),
    ("python","result = []\\nfor item in items:\\n    if item not in seen:\\n        seen.add(item)\\n        result.append(item)","result = list(dict.fromkeys(items))"),
    ("python","s = ''\\nfor name in names:\\n    s += name + ', '\\ns = s[:-2]","s = ', '.join(names)"),
    ("python","def foo():\\n    pass\\n# 100 lines later\\ndef bar():\\n    pass","class Processor:\\n    def foo(self): pass\\n    def bar(self): pass"),
    ("python","def get_info():\\n    d={}\\n    d['name']=get_name()\\n    d['age']=get_age()\\n    d['city']=get_city()\\n    return d","def get_info():\\n    return {'name':get_name(),'age':get_age(),'city':get_city()}"),
    ("python","def check(n): return True if n>0 else False","def check(n): return n>0"),
    ("python","with open('f.txt') as f: data=f.read()\\n# ... 50 lines ...\\nwith open('f.txt') as f: data2=f.read()","data = open('f.txt').read()\\n# process once, reuse"),
    ("python","if type(x)==int: pass","if isinstance(x,int): pass"),
    ("python","for i in range(len(items)): print(items[i])","for item in items: print(item)"),
    ("python","def add(a,b): return a+b\\ndef sub(a,b): return a-b\\ndef mul(a,b): return a*b\\ndef div(a,b): return a/b","import operator\\nadd=operator.add;sub=operator.sub;mul=operator.mul;div=operator.truediv"),
    ("python","x = 3.14159 * r * r","from math import pi\\nx = pi * r * r"),
    ("python","try:\\n    result = risky()\\nexcept:\\n    pass","try:\\n    result = risky()\\nexcept Exception as e:\\n    log_error(e)"),
    ("python","if a==True: pass","if a: pass"),
    ("python","x = x + 1","x += 1"),
    ("python","def process():\\n    global x\\n    x = x * 2","def process(x):\\n    return x * 2"),
    ("python","def f():\\n    import os\\n    return os.listdir('.')","import os\\ndef f():\\n    return os.listdir('.')"),
    ("python","def read_file():\n    with open('data.txt') as f:\n        return f.read()\n\ndef parse_data():\n    data = read_file()\n    return json.loads(data)\n\ndef process():\n    data = parse_data()\n    for item in data:\n        print(item)","def process():\n    with open('data.txt') as f:\n        data = json.load(f)\n    for item in data:\n        print(item)"),
    # JavaScript refactoring  
    ("javascript","function add(a,b){return a+b}","const add=(a,b)=>a+b"),
    ("javascript","if(arr.indexOf(x)>-1)","if(arr.includes(x))"),
    ("javascript","var x=5;var y=10;var z=15","const x=5,y=10,z=15"),
    ("javascript","for(var i=0;i<arr.length;i++){console.log(arr[i])}","arr.forEach(x=>console.log(x))"),
    ("javascript","function double(arr){const r=[];for(let i=0;i<arr.length;i++){r.push(arr[i]*2)}return r}","const double=arr=>arr.map(x=>x*2)"),
    ("javascript","function getAdults(users){const r=[];for(let i=0;i<users.length;i++){if(users[i].age>=18)r.push(users[i])}return r}","const getAdults=users=>users.filter(u=>u.age>=18)"),
    ("javascript","const x=new Date().getFullYear()","const x=new Date().getFullYear() // ok, but: const year = new Date().getFullYear()"),
    ("javascript","function f(p){if(p==null||p==undefined)return}","function f(p){if(p==null)return}"),
    ("javascript","let a=10;a=a+5","let a=10;a+=5"),
    ("javascript","const nums=[1,2,3,4];const doubled=[];for(let n of nums){doubled.push(n*2)}","const nums=[1,2,3,4];const doubled=nums.map(n=>n*2)"),
    ("javascript","function User(name,age){this.name=name;this.age=age}","class User{constructor(name,age){this.name=name;this.age=age}}"),
    ("javascript","const result=items.reduce(function(acc,item){return acc+item},0)","const result=items.reduce((acc,item)=>acc+item,0)"),
    ("javascript","if(condition){return true}else{return false}","return !!condition"),
    ("javascript","const http=require('http');const fs=require('fs');const path=require('path')","import http from 'http';import fs from 'fs';import path from 'path'"),
    ("javascript","function doStuff(){if(!x)return null;if(!x.y)return null;return x.y.z}","function doStuff(){return x?.y?.z??null}"),
    # Java refactoring
    ("java","if (x == true) { return true; } else { return false; }","return x;"),
    ("java","List<String> list = new ArrayList<String>();","var list = new ArrayList<String>();"),
    ("java","public int calc(int a,int b,int c){return a+b+c;}","public int sum(int... nums){return Arrays.stream(nums).sum();}"),
    ("java","String s = \"\"; for(String n:names){s+=n+\",\";} s=s.substring(0,s.length()-1);","String s = String.join(\",\", names);"),
    ("java","for(int i=0;i<items.size();i++){System.out.println(items.get(i));}","for(var item:items){System.out.println(item);}"),
    ("java","if(obj != null){obj.doSomething();}","if(Optional.ofNullable(obj).isPresent()){obj.doSomething();}"),
    ("java","int x; try{x=Integer.parseInt(s);}catch(Exception e){x=0;}","int x = Optional.ofNullable(s).map(Integer::parseInt).orElse(0);"),
    ("java","public boolean isEmpty(String s){if(s==null||s.length()==0)return true;return false;}","public boolean isEmpty(String s){return s==null||s.isEmpty();}"),
    ("java","public void save(User u){if(u.getName()!=null){db.save(u);}}","public void save(User u){Optional.ofNullable(u).filter(u->u.getName()!=null).ifPresent(db::save);}"),
    ("java","Map<String,Integer> map=new HashMap<>(); map.put(\"a\",1); map.put(\"b\",2);","var map=Map.of(\"a\",1,\"b\",2);"),
    ("java","int[] arr = new int[5]; arr[0]=1; arr[1]=2; arr[2]=3; arr[3]=4; arr[4]=5;","int[] arr = {1,2,3,4,5};"),
    ("java","public int getCount(){return this.counter++;}","private int counter = 0;\\npublic int getCount(){return counter++;}"),
    ("java","try{Thread.sleep(1000);}catch(Exception e){}","try{Thread.sleep(Duration.ofSeconds(1));}catch(InterruptedException e){Thread.currentThread().interrupt();}"),
    ("java","BufferedReader br=new BufferedReader(new FileReader(\"f.txt\"));String l;while((l=br.readLine())!=null){System.out.println(l);}br.close();","try(var br=new BufferedReader(new FileReader(\"f.txt\"))){br.lines().forEach(System.out::println);}"),
    ("java","public void process(){if(debug){System.out.println(\"debug\");}}","import java.util.logging.Logger;\\nprivate static final Logger LOG=Logger.getLogger(\"...\");\\npublic void process(){LOG.fine(\"debug\");}"),
    # Go refactoring
    ("go","if err != nil { return err }\\nif err2 != nil { return err2 }","return err // or use errgroup"),
    ("go","var s string\\nfor _,n:=range names{s+=n+\",\"}\\ns=strings.TrimSuffix(s,\",\")","s:=strings.Join(names,\",\")"),
    ("go","for i:=0;i<len(items);i++{fmt.Println(items[i])}","for _,item:=range items{fmt.Println(item)}"),
    ("go","type Person struct {Name string;Age int}","type Person struct{\\nName string\\nAge int\\n}"),
    ("go","func add(a int,b int)int{return a+b}","func add(a,b int)int{return a+b}"),
    ("go","x:=10\\nx=x+5","x:=10\\nx+=5"),
    ("go","val,ok:=m[\"key\"]\\nif ok{fmt.Println(val)}","if val,ok:=m[\"key\"];ok{fmt.Println(val)}"),
    ("go","if len(slice)==0{return true}","return len(slice)==0"),
    ("go","var i int\\nfor i=0;i<10;i++{fmt.Println(i)}","for i:=range 10{fmt.Println(i)}"),
    ("go","data,err:=os.ReadFile(\"f.txt\")\\nif err!=nil{panic(err)}\\ncontent:=string(data)","import _ \"embed\"\\n//go:embed f.txt\\nvar content string"),
    ("go","func(double x)float64{return x*2}","func double(x float64)float64{return x*2} // named function"),
    ("go","result:=0\\nfor _,v:=range values{result=result+v}","for _,v:=range values{result+=v}"),
    ("go","a:=make([]int,0)\\nfor i:=0;i<5;i++{a=append(a,i)}","a:=[]int{0,1,2,3,4}"),
    ("go","var x = 10\\nvar y = 20","x,y:=10,20"),
    ("go","if x>0{return true}else{return false}","return x>0"),
    # TypeScript refactoring
    ("typescript","function add(a:any,b:any){return a+b}","function add(a:number,b:number):number{return a+b}"),
    ("typescript","interface Person{name:string}","interface Person{readonly name:string}"),
    ("typescript","const x:Array<string>=[]","const x:string[]=[]"),
    ("typescript","if(x!==null && x!==undefined)","if(x!=null)"),
    ("typescript","function f(o:any){return o.name}","function f(o:{name:string}){return o.name}"),
    ("typescript","const result=items.reduce(function(a,b){return a+b},0)","const result=items.reduce((a,b)=>a+b,0)"),
    ("typescript","function f(callback:Function){}","function f(callback:()=>void){}"),
    ("typescript","let x:number=5","const x=5"),
    ("typescript","enum Color{Red=0,Green=1,Blue=2}","const enum Color{Red,Green,Blue}"),
    ("typescript","if(arr.indexOf(x)!==-1)","if(arr.includes(x))"),
    ("typescript","function f(){return new Promise((resolve,reject)=>{resolve(5)})}","async function f(){return 5}"),
    ("typescript","const p:Promise<number>=new Promise((r)=>r(5))","const p:Promise<number>=Promise.resolve(5)"),
    ("typescript","interface A{foo():void} class B implements A{foo():void{}}","interface A{foo():void} class B implements A{foo():void{}}"),
    ("typescript","function f(a:number|undefined){return a||0}","function f(a?:number){return a??0}"),
    ("typescript","type T=string|number;const x:T=\"hello\"","type T=string|number;const x:T=\"hello\""),
]
for l,bad,good in pairs_ref:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)

print(f"Total: {len(D)} pairs")
with open(O,"w",encoding="utf-8") as f:
    json.dump(D,f,ensure_ascii=False,indent=2)
print(f"Written to {O}")

# === Add more security pairs ===
pairs_sec2 = [
    # CSRF
    ("python","@app.route(\"/t\",methods=[\"POST\"])\\ndef t():\\n    a=request.form[\"a\"]\\n    t=request.form[\"t\"]\\n    transfer(current_user,t,a)\\n    return \"OK\"","from flask_wtf.csrf import CSRFProtect\\ncsrf=CSRFProtect(app)\\n@app.route(\"/t\",methods=[\"POST\"])\\ndef t():\\n    a=request.form[\"a\"]\\n    t=request.form[\"t\"]\\n    transfer(current_user,t,a)\\n    return \"OK\""),
    ("python","@app.route(\"/del\",methods=[\"POST\"])\\ndef d():\\n    db.execute(\"DELETE FROM users WHERE id=?\",(current_user.id,))\\n    return redirect(\"/\")","@app.route(\"/del\",methods=[\"POST\"])\\ndef d():\\n    if request.form.get(\"csrf\")!=session.get(\"csrf\"):abort(403)\\n    db.execute(\"DELETE FROM users WHERE id=?\",(current_user.id,))\\n    return redirect(\"/\")"),
    ("python","@app.route(\"/ch_email\",methods=[\"POST\"])\\ndef ch():\\n    update_email(current_user.id,request.form[\"e\"])\\n    return \"ok\"","@app.route(\"/ch_email\",methods=[\"POST\"])\\ndef ch():\\n    if request.form.get(\"csrf\")!=session.pop(\"csrf\",None):abort(403)\\n    update_email(current_user.id,request.form[\"e\"])\\n    return \"ok\""),
    ("javascript","app.post(\"/t\",(r,s)=>{db.run(\"INSERT INTO t(u,to,amt) VALUES(?,?,?)\",[r.session.u,r.body.to,r.body.amt]);s.send(\"OK\")})","const csrf=require(\"csurf\");\\napp.post(\"/t\",csrf({cookie:true}),(r,s)=>{db.run(\"INSERT INTO t(u,to,amt) VALUES(?,?,?)\",[r.session.u,r.body.to,r.body.amt]);s.send(\"OK\")})"),
    ("javascript","app.post(\"/up\",(r,s)=>{db.query(\"UPDATE users SET email=? WHERE id=?\",[r.body.e,r.user.id]);s.redirect(\"/p\")})","app.post(\"/up\",csrf(),(r,s)=>{db.query(\"UPDATE users SET email=? WHERE id=?\",[r.body.e,r.user.id]);s.redirect(\"/p\")})"),
    ("javascript","app.post(\"/sub\",(r,s)=>{db.run(\"UPDATE users SET sub=1 WHERE id=?\",[r.session.u]);s.json({ok:1})})","app.post(\"/sub\",csrf({cookie:true}),(r,s)=>{db.run(\"UPDATE users SET sub=1 WHERE id=?\",[r.session.u]);s.json({ok:1})})"),
    ("java","@PostMapping(\"/t\")String t(@RequestParam String to,@RequestParam BigDecimal a){transferService.transfer(getUser(),to,a);return\"ok\"}","@Configuration @EnableWebSecurity\\nclass Config extends WebSecurityConfigurerAdapter{\\n  @Override protected void configure(HttpSecurity h){h.csrf().csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse());}}"),
    ("java","@PostMapping(\"/cp\")ResponseEntity<?>cp(@RequestParam String p){userService.updatePassword(getUser(),p);return ResponseEntity.ok().build()}","// Thymeleaf: <input type=\"hidden\" th:name=\"${_csrf.parameterName}\" th:value=\"${_csrf.token}\" />"),
    ("go","func t(w http.ResponseWriter,r*http.Request){to:=r.FormValue(\"to\");amt:=r.FormValue(\"amt\");transfer(getUser(r),to,amt);w.Write([]byte(\"OK\"))}","import \"github.com/gorilla/csrf\"\\n// Router: csrf.Protect([]byte(\"key\"),csrf.Secure(false))(r)"),
    ("go","func del(w http.ResponseWriter,r*http.Request){uid:=r.Context().Value(\"uid\").(int);db.Exec(\"DELETE FROM users WHERE id=?\",uid);w.Write([]byte(\"ok\"))}","// CSRF middleware ile token kontrolu"),
    ("web","<form action=\"/t\" method=\"POST\"><input name=\"to\"><input name=\"amt\"><button>Gonder</button></form>","<form action=\"/t\" method=\"POST\"><input type=\"hidden\" name=\"csrf\" value=\"{{csrf_token}}\"><input name=\"to\"><input name=\"amt\"><button>Gonder</button></form>"),
    # SSRF
    ("python","@app.route(\"/f\")\\ndef f():\\n    url=request.args.get(\"url\")\\n    return requests.get(url).text","ALLOWED=[\"api.x.com\"]\\n@app.route(\"/f\")\\ndef f():\\n    url=request.args.get(\"url\")\\n    if urlparse(url).hostname not in ALLOWED:return \"red\",403\\n    return requests.get(url,timeout=5).text"),
    ("python","@app.route(\"/d\")\\ndef d():\\n    p=request.args.get(\"p\")\\n    return urlopen(f\"http://internal:8080/{p}\").read()","@app.route(\"/d\")\\ndef d():\\n    p=request.args.get(\"p\")\\n    if \"..\" in p or \"/\" in p:return \"invalid\",400\\n    return urlopen(f\"http://internal:8080/{p}\",timeout=5).read()"),
    ("python","def proxy():\\n    t=request.headers.get(\"X-Target\")\\n    return requests.post(t,data=request.get_data()).content","def proxy():\\n    t=request.headers.get(\"X-Target\")\\n    if t not in [\"https://api.p.com\"]:return \"red\",403\\n    return requests.post(t,data=request.get_data(),timeout=10).content"),
    ("javascript","app.get(\"/f\",async(r,s)=>{const u=r.query.u;const d=await(await fetch(u)).text();s.send(d)})","app.get(\"/f\",async(r,s)=>{const u=r.query.u;try{const p=new URL(u);if([\"localhost\",\"127.0.0.1\",\"0.0.0.0\"].includes(p.hostname))return s.status(403).send(\"no\");const d=await(await fetch(u,{signal:AbortSignal.timeout(5000)})).text();s.send(d)}catch{s.status(400).send(\"invalid\")}})"),
    ("javascript","app.post(\"/p\",(r,s)=>{http.get(r.body.t,(re)=>re.pipe(s))})","app.post(\"/p\",(r,s)=>{const p=new URL(r.body.t);if(/^(127|10|172\\.(1[6-9]|2\\\\d|3[01])|192\\.168)/.test(p.hostname))return s.status(403).send(\"no\");http.get(r.body.t,{timeout:5000},(re)=>re.pipe(s))})"),
    ("java","@GetMapping(\"/f\")String f(@RequestParam String u)throws IOException{URL url=new URL(u);try(var r=new BufferedReader(new InputStreamReader(url.openStream()))){return r.lines().collect(Collectors.joining())}}","@GetMapping(\"/f\")String f(@RequestParam String u)throws IOException{URI uri=new URI(u);String h=uri.getHost();if(h.equals(\"localhost\")||h.startsWith(\"10.\"))throw new SecurityException();HttpURLConnection c=(HttpURLConnection)uri.toURL().openConnection();c.setConnectTimeout(5000);try(var r=new BufferedReader(new InputStreamReader(c.getInputStream()))){return r.lines().collect(Collectors.joining())}}"),
    ("java","@PostMapping(\"/pi\")ResponseEntity<byte[]>pi(@RequestParam String u)throws IOException{return ResponseEntity.ok(IOUtils.toByteArray(new URL(u)))}","@PostMapping(\"/pi\")ResponseEntity<byte[]>pi(@RequestParam String u)throws IOException{URI uri=new URI(u);InetAddress a=InetAddress.getByName(uri.getHost());if(a.isSiteLocalAddress()||a.isLoopbackAddress())return ResponseEntity.status(403).build();HttpURLConnection c=(HttpURLConnection)uri.toURL().openConnection();c.setConnectTimeout(3000);return ResponseEntity.ok(IOUtils.toByteArray(c.getInputStream()))}"),
    ("go","func f(w http.ResponseWriter,r*http.Request){url:=r.URL.Query().Get(\"u\");resp,_:=http.Get(url);defer resp.Body.Close();io.Copy(w,resp.Body)}","func f(w http.ResponseWriter,r*http.Request){raw:=r.URL.Query().Get(\"u\");p,_:=url.Parse(raw);addrs,_:=net.LookupHost(p.Hostname());for_,a:=range addrs{ip:=net.ParseIP(a);if ip.IsPrivate()||ip.IsLoopback(){http.Error(w,\"no\",403);return}}c:=&http.Client{Timeout:5*time.Second};resp,err:=c.Get(raw);if err!=nil{http.Error(w,err.Error(),500);return}defer resp.Body.Close();io.Copy(w,resp.Body)}"),
    ("go","func a(w http.ResponseWriter,r*http.Request){u:=r.FormValue(\"u\");resp,_:=http.Get(u);defer resp.Body.Close();d,_:=ioutil.ReadAll(resp.Body);w.Write(d)}","func a(w http.ResponseWriter,r*http.Request){u:=r.FormValue(\"u\");p,_:=url.Parse(u);if!strings.HasPrefix(p.Host,\"cdn.x.com\"){http.Error(w,\"no\",403);return}c:=&http.Client{Timeout:5*time.Second};resp,err:=c.Get(u);if err!=nil{http.Error(w,\"err\",502);return}defer resp.Body.Close();d,_:=ioutil.ReadAll(resp.Body);w.Write(d)}"),
    ("web","<?php $url=$_GET[\"img\"];$d=file_get_contents($url);header(\"Content-Type: image/jpeg\");echo $d;?>","<?php $url=$_GET[\"img\"];$p=parse_url($url);$b=[\"127.0.0.1\",\"localhost\"];if(in_array($p[\"host\"],$b)||preg_match(\"/^10\\\\.|^192\\.168\\\\./\",$p[\"host\"])){http_response_code(403);die();}$ctx=stream_context_create([\"http\"=>[\"timeout\"=>5]]);$d=file_get_contents($url,false,$ctx);header(\"Content-Type: image/jpeg\");echo $d;?>"),
    # IDOR
    ("python","@app.route(\"/api/user/<int:uid>\")\\ndef get(uid):\\n    u=db.execute(\"SELECT * FROM users WHERE id=?\",(uid,)).fetchone()\\n    return jsonify(dict(u))","@app.route(\"/api/user/<int:uid>\")\\ndef get(uid):\\n    if uid!=current_user.id and not current_user.is_admin:return \"no\",403\\n    u=db.execute(\"SELECT * FROM users WHERE id=?\",(uid,)).fetchone()\\n    return jsonify(dict(u))"),
    ("python","@app.route(\"/api/order/<int:oid>\")\\ndef get_order(oid):\\n    o=db.execute(\"SELECT * FROM orders WHERE id=?\",(oid,)).fetchone()\\n    return jsonify(dict(o))","@app.route(\"/api/order/<int:oid>\")\\ndef get_order(oid):\\n    o=db.execute(\"SELECT * FROM orders WHERE id=? AND user_id=?\",(oid,current_user.id)).fetchone()\\n    if not o:return \"no\",404\\n    return jsonify(dict(o))"),
    ("python","@app.route(\"/api/invoice/<iid>\")\\ndef inv(iid):\\n    i=db.execute(\"SELECT * FROM invoices WHERE id=?\",(iid,)).fetchone()\\n    return jsonify(dict(i))","@app.route(\"/api/invoice/<iid>\")\\ndef inv(iid):\\n    i=db.execute(\"SELECT * FROM invoices WHERE id=? AND user_id=?\",(iid,current_user.id)).fetchone()\\n    if not i:return \"no\",404\\n    return jsonify(dict(i))"),
    ("javascript","app.get(\"/api/users/:id\",(r,s)=>{db.get(\"SELECT * FROM users WHERE id=?\",[r.params.id],(e,u)=>s.json(u))})","app.get(\"/api/users/:id\",(r,s)=>{if(r.params.id!=r.user.id&&!r.user.isAdmin)return s.status(403).json({e:\"no\"});db.get(\"SELECT * FROM users WHERE id=?\",[r.params.id],(e,u)=>s.json(u))})"),
    ("javascript","app.delete(\"/api/orders/:id\",(r,s)=>{db.run(\"DELETE FROM orders WHERE id=?\",[r.params.id]);s.json({ok:1})})","app.delete(\"/api/orders/:id\",(r,s)=>{db.run(\"DELETE FROM orders WHERE id=? AND user_id=?\",[r.params.id,r.user.id],function(e){if(this.changes===0)return s.status(404).json({e:\"no\"});s.json({ok:1})})})"),
    ("javascript","app.put(\"/api/docs/:id\",(r,s)=>{db.run(\"UPDATE docs SET content=? WHERE id=?\",[r.body.c,r.params.id]);s.json({ok:1})})","app.put(\"/api/docs/:id\",(r,s)=>{db.run(\"UPDATE docs SET content=? WHERE id=? AND owner_id=?\",[r.body.c,r.params.id,r.user.id],function(e){if(this.changes===0)return s.status(403).json({e:\"no\"});s.json({ok:1})})})"),
    ("java","@GetMapping(\"/api/users/{id}\")User get(@PathVariable Long id){return repo.findById(id).orElseThrow()}","@GetMapping(\"/api/users/{id}\")User get(@PathVariable Long id){User c=getCurrentUser();if(!c.getId().equals(id)&&!c.isAdmin())throw new AccessDeniedException();return repo.findById(id).orElseThrow()}"),
    ("java","@DeleteMapping(\"/api/orders/{id}\")void cancel(@PathVariable Long id){orderRepo.deleteById(id)}","@DeleteMapping(\"/api/orders/{id}\")void cancel(@PathVariable Long id){Order o=orderRepo.findById(id).orElseThrow();if(!o.getUserId().equals(getCurrentUser().getId()))throw new AccessDeniedException();orderRepo.delete(o)}"),
    ("go","func get(w http.ResponseWriter,r*http.Request){vars:=mux.Vars(r);id:=vars[\"id\"];var u User;db.Get(&u,\"SELECT * FROM users WHERE id=?\",id);json.NewEncoder(w).Encode(u)}","func get(w http.ResponseWriter,r*http.Request){vars:=mux.Vars(r);id:=vars[\"id\"];uid:=r.Context().Value(\"uid\").(string);if id!=uid{http.Error(w,\"no\",403);return}var u User;db.Get(&u,\"SELECT * FROM users WHERE id=?\",id);json.NewEncoder(w).Encode(u)}"),
    ("go","func inv(w http.ResponseWriter,r*http.Request){id:=r.URL.Query().Get(\"id\");var i Invoice;db.Get(&i,\"SELECT * FROM invoices WHERE id=?\",id);json.NewEncoder(w).Encode(i)}","func inv(w http.ResponseWriter,r*http.Request){id:=r.URL.Query().Get(\"id\");uid:=r.Context().Value(\"uid\").(int);var i Invoice;err:=db.Get(&i,\"SELECT * FROM invoices WHERE id=? AND user_id=?\",id,uid);if err!=nil{http.Error(w,\"no\",404);return}json.NewEncoder(w).Encode(i)}"),
    ("web","<?php $uid=$_GET[\"uid\"];$s=$db->prepare(\"SELECT * FROM users WHERE id=?\");$s->execute([$uid]);echo json_encode($s->fetch());?>","<?php session_start();$uid=$_GET[\"uid\"];if($uid!=$_SESSION[\"uid\"]&&!$_SESSION[\"admin\"]){http_response_code(403);die();}$s=$db->prepare(\"SELECT * FROM users WHERE id=?\");$s->execute([$uid]);echo json_encode($s->fetch());?>"),
]
for l,bad,good in pairs_sec2:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

print(f"After batch2: {len(D)}")

# ===== Add remaining security pairs (path traversal, command inj, deser, eval, proto, cors, creds, redirect, headers, randomness, password, jwt, disclosure) =====
pairs_sec3 = [
    # Path Traversal
    ("python","@app.route(\"/files/<f>\")\\ndef get(f):\\n    return open(f\"/var/www/uploads/{f}\").read()","import os\\n@app.route(\"/files/<f>\")\\ndef get(f):\\n    base=\"/var/www/uploads\"\\n    full=os.path.normpath(os.path.join(base,f))\\n    if not full.startswith(base):return \"no\",400\\n    return open(full).read()"),
    ("python","def load(u):return open(f\"avatars/{u}.png\",\"rb\").read()","import re\\ndef load(u):\\n    if not re.match(r\"^[a-zA-Z0-9_]+\",u):return None\\n    return open(f\"avatars/{u}.png\",\"rb\").read()"),
    ("python","@app.route(\"/assets/<path:p>\")\\ndef serve(p):\\n    return send_file(f\"assets/{p}\")","import os\\n@app.route(\"/assets/<path:p>\")\\ndef serve(p):\\n    base=os.path.abspath(\"assets\")\\n    full=os.path.normpath(os.path.join(base,p))\\n    if not full.startswith(base):return \"no\",400\\n    return send_file(full)"),
    ("javascript","app.get(\"/dl\",(r,s)=>{s.sendFile(path.join(__dirname,\"public\",r.query.f))})","app.get(\"/dl\",(r,s)=>{const f=r.query.f;const sp=path.normalize(path.join(__dirname,\"public\",f));if(!sp.startsWith(path.join(__dirname,\"public\")))return s.status(400).send(\"no\");s.sendFile(sp)})"),
    ("javascript","app.get(\"/read/*\",(r,s)=>{fs.readFile(\"/data/\"+r.params[0],\"utf8\",(e,d)=>s.send(d))})","app.get(\"/read/*\",(r,s)=>{const p=r.params[0];const base=\"/data\";const full=path.resolve(base,p);if(!full.startsWith(path.resolve(base)))return s.status(400).send(\"no\");fs.readFile(full,\"utf8\",(e,d)=>{if(e)return s.status(404).send(\"no\");s.send(d)})})"),
    ("java","@GetMapping(\"/files/{n}\")byte[]get(@PathVariable String n)throws IOException{return Files.readAllBytes(Paths.get(\"/var/data/\"+n))}","@GetMapping(\"/files/{n}\")byte[]get(@PathVariable String n)throws IOException{Path base=Paths.get(\"/var/data\").toRealPath();Path r=base.resolve(n).normalize();if(!r.startsWith(base))throw new SecurityException();return Files.readAllBytes(r)}"),
    ("java","Resource load(String n){return new FileSystemResource(\"/images/\"+n)}","Resource load(String n){try{Path base=Paths.get(\"/images\").toRealPath();Path r=base.resolve(n).normalize();if(!r.startsWith(base))throw new SecurityException();return new FileSystemResource(r.toFile())}catch(IOException e){throw new RuntimeException(e)}}"),
    ("go","func dl(w http.ResponseWriter,r*http.Request){f:=r.URL.Query().Get(\"f\");http.ServeFile(w,r,\"/data/\"+f)}","func dl(w http.ResponseWriter,r*http.Request){f:=r.URL.Query().Get(\"f\");base:=\"/data\";full:=filepath.Join(base,f);if!strings.HasPrefix(filepath.Clean(full),base){http.Error(w,\"no\",400);return}http.ServeFile(w,r,full)}"),
    ("go","func read(w http.ResponseWriter,r*http.Request){p:=r.URL.Path[6:];d,_:=ioutil.ReadFile(p);w.Write(d)}","func read(w http.ResponseWriter,r*http.Request){p:=r.URL.Path[6:];base:=\"/safe\";full:=filepath.Join(base,p);if!strings.HasPrefix(filepath.Clean(full),base){http.Error(w,\"no\",400);return}d,_:=ioutil.ReadFile(full);w.Write(d)}"),
    ("web","<?php $f=$_GET[\"f\"];$c=file_get_contents(\"pages/\".$f);echo $c;?>","<?php $f=$_GET[\"f\"];$f=basename($f);$b=realpath(\"pages\");$fu=realpath(\"pages/\".$f);if(!$fu||strpos($fu,$b)!==0){http_response_code(403);die();}echo file_get_contents($fu);?>"),
    # Command Injection
    ("python","def ping(ip):return subprocess.check_output(f\"ping {ip}\",shell=True).decode()","def ping(ip):\\n    if not re.match(r\"^[\\\\d.]+\",ip):return \"invalid\"\\n    return subprocess.check_output([\"ping\",\"-c\",\"1\",ip],timeout=10).decode()"),
    ("python","def run(n):os.system(f\"./scripts/{n}.sh\")","def run(n):\\n    if not re.match(r\"^[a-zA-Z0-9_-]+\",n):raise ValueError()\\n    subprocess.run([\"./scripts/\"+n+\".sh\"],timeout=30)"),
    ("python","def conv(f):subprocess.call(f\"ffmpeg -i {f} o.mp4\",shell=True)","def conv(f):subprocess.call([\"ffmpeg\",\"-i\",f,\"o.mp4\"])"),
    ("javascript","app.get(\"/ping\",(r,s)=>{exec(`ping -c 1 ${r.query.ip}`,(e,o)=>s.send(o))})","app.get(\"/ping\",(r,s)=>{const ip=r.query.ip;if(!/^[\\\\d.]+$/.test(ip))return s.status(400).send(\"no\");execFile(\"ping\",[\"-c\",\"1\",ip],{timeout:5000},(e,o)=>s.send(o))})"),
    ("javascript","app.post(\"/b\",(r,s)=>{exec(`mysqldump ${r.body.d}>/tmp/b.sql`,()=>s.send(\"ok\"))})","app.post(\"/b\",(r,s)=>{const db=r.body.d;if(!/^[a-zA-Z0-9_]+$/.test(db))return s.status(400).send(\"no\");execFile(\"mysqldump\",[db],{timeout:30000}).stdout.pipe(fs.createWriteStream(\"/tmp/b.sql\"));s.send(\"ok\")})"),
    ("java","@GetMapping(\"/ping\")String ping(@RequestParam String h)throws IOException{return new String(Runtime.getRuntime().exec(\"ping \"+h).getInputStream().readAllBytes())}","@GetMapping(\"/ping\")String ping(@RequestParam String h)throws IOException{if(!h.matches(\"^[\\\\\\\\d.]+$\"))throw new IllegalArgumentException();return new String(new ProcessBuilder(\"ping\",\"-c\",\"1\",h).start().getInputStream().readAllBytes())}"),
    ("java","String run(String n)throws IOException{return new String(Runtime.getRuntime().exec(\"bash /scripts/\"+n).getInputStream().readAllBytes())}","String run(String n)throws IOException{if(!n.matches(\"^[a-zA-Z0-9_-]+$\"))throw new IllegalArgumentException();return new String(new ProcessBuilder(\"bash\",\"/scripts/\"+n).start().getInputStream().readAllBytes())}"),
    ("go","func ping(w http.ResponseWriter,r*http.Request){ip:=r.URL.Query().Get(\"ip\");out,_:=exec.Command(\"sh\",\"-c\",\"ping \"+ip).Output();w.Write(out)}","func ping(w http.ResponseWriter,r*http.Request){ip:=r.URL.Query().Get(\"ip\");if!regexp.MustCompile(`^[\\\\d.]+$`).MatchString(ip){http.Error(w,\"no\",400);return}out,_:=exec.Command(\"ping\",\"-c\",\"1\",ip).Output();w.Write(out)}"),
    ("go","func conv(w http.ResponseWriter,r*http.Request){i:=r.FormValue(\"i\");exec.Command(\"bash\",\"-c\",fmt.Sprintf(\"ffmpeg -i %s o.mp4\",i)).Run()}","func conv(w http.ResponseWriter,r*http.Request){i:=r.FormValue(\"i\");exec.Command(\"ffmpeg\",\"-i\",i,\"o.mp4\").Run()}"),
    ("web","<?php $d=$_GET[\"d\"];$o=shell_exec(\"ping \".$d);echo \"<pre>$o</pre>\";?>","<?php $d=$_GET[\"d\"];if(!preg_match(\"/^[a-zA-Z0-9.]+$/\",$d))die();$o=shell_exec(escapeshellcmd(\"ping \".$d));echo \"<pre>\".htmlspecialchars($o).\"</pre>\";?>"),
    # Insecure Deserialization
    ("python","import pickle\\ndef load(d):return pickle.loads(base64.b64decode(d))","import json\\ndef load(d):return json.loads(base64.b64decode(d).decode())"),
    ("python","def restore(d):return yaml.load(d)","def restore(d):return yaml.safe_load(d)"),
    ("javascript","app.post(\"/d\",(r,s)=>{const o=eval(\"(\"+r.body.j+\")\");s.json(o)})","app.post(\"/d\",(r,s)=>{s.json(r.body)})"),
    ("javascript","app.post(\"/res\",(r,s)=>{const d=JSON.parse(r.body.d);new Function(\"return \"+d.c)();s.send(\"ok\")})","app.post(\"/res\",(r,s)=>{const d=JSON.parse(r.body.d);if(typeof d.c!=\"string\")return s.status(400).send(\"no\");s.send(\"ok\")})"),
    ("java","@PostMapping(\"/d\")Object d(@RequestBody byte[] d)throws Exception{return new ObjectInputStream(new ByteArrayInputStream(d)).readObject()}","@PostMapping(\"/d\")Object d(@RequestBody byte[] d)throws Exception{ValidatingObjectInputStream o=new ValidatingObjectInputStream(new ByteArrayInputStream(d));o.accept(User.class);return o.readObject()}"),
    ("java","@PostMapping(\"/i\")void i(@RequestBody String x)throws Exception{XMLDecoder d=new XMLDecoder(new ByteArrayInputStream(x.getBytes()));process(d.readObject())}","@PostMapping(\"/i\")void i(@RequestBody String j)throws Exception{process(new ObjectMapper().readValue(j,ImportData.class))}"),
    ("go","func res(w http.ResponseWriter,r*http.Request){data,_:=ioutil.ReadAll(r.Body);var obj map[string]interface{};json.Unmarshal(data,&obj)}","func res(w http.ResponseWriter,r*http.Request){data,_:=ioutil.ReadAll(r.Body);var obj UserConfig;if err:=json.Unmarshal(data,&obj);err!=nil{http.Error(w,\"inv\",400)}}"),
    ("web","<?php $data=unserialize($_COOKIE[\"s\"]);echo \"Hi \".$data[\"n\"];?>","<?php $data=json_decode($_COOKIE[\"s\"],true);if(!$data)$data=[\"n\"=>\"Misafir\"];echo \"Hi \".htmlspecialchars($data[\"n\"]);?>"),
    # Unsafe Eval
    ("python","def calc(e):return eval(e)","import ast\\ndef calc(e):\\n    t=ast.parse(e,mode=\"eval\")\\n    for n in ast.walk(t):\\n        if not isinstance(n,(ast.Expression,ast.BinOp,ast.UnaryOp,ast.Constant,ast.Add,ast.Sub,ast.Mult,ast.Div)):raise ValueError()\\n    return eval(compile(t,\"<string>\",\"eval\"))"),
    ("python","def exec_code(c):exec(c)","def exec_code(c):exec(c,{\"__builtins__\":{}})"),
    ("javascript","function c(i){return eval(i)}","function c(i){return Function('\"use strict\";return('+JSON.stringify(i)+')')()}"),
    ("javascript","app.post(\"/t\",(r,s)=>{s.json({r:eval(r.body.e)})})","app.post(\"/t\",(r,s)=>{try{s.json({r:Function('\"use strict\";return('+r.body.e+')')()})}catch{s.status(400).json({e:\"no\"})}})"),
    ("javascript","app.get(\"/run\",(r,s)=>{s.send(String(new Function(r.query.c)()))})","app.get(\"/run\",(r,s)=>{s.status(403).send(\"kapali\")})"),
    ("java","@PostMapping(\"/e\")Object e(@RequestBody String c)throws Exception{ScriptEngine e=new ScriptEngineManager().getEngineByName(\"JavaScript\");return e.eval(c)}","@PostMapping(\"/e\")Object e(@RequestBody String c)throws Exception{Bindings b=new ScriptEngineManager().getEngineByName(\"JavaScript\").createBindings();return ((ScriptEngineManager)(...)).eval(\"JSON.parse('\"+c.replaceAll(\"[\\\"']\",\"\")+\"')\",b)}"),
    ("go","type C struct{Code string `json:\"code\"`};func ex(w http.ResponseWriter,r*http.Request){var c C;json.NewDecoder(r.Body).Decode(&c);w.Write([]byte(run(c.Code)))}","func ex(w http.ResponseWriter,r*http.Request){var c C;json.NewDecoder(r.Body).Decode(&c);m:=map[string]func()string{\"ping\":func()string{return\"pong\"}};if fn,ok:=m[c.Code];ok{w.Write([]byte(fn()))}else{http.Error(w,\"no\",400)}}"),
    ("web","<?php $code=$_POST[\"c\"];eval($code);?>","<?php $code=$_POST[\"c\"];$a=[\"strtoupper\",\"strtolower\"];if(in_array($code,$a))echo $code(\"t\");else echo \"no\";?>"),
    # Prototype Pollution
    ("javascript","function m(t,s){for(const k in s){t[k]=s[k]}return t}","function m(t,s){for(const k in s){if(k==\"__proto__\"||k==\"constructor\")continue;t[k]=s[k]}return t}"),
    ("javascript","app.post(\"/u\",(r,s)=>{Object.assign(r.user,r.body);s.json(r.user)})","app.post(\"/u\",(r,s)=>{const safe=[\"name\",\"email\"];for(const k of Object.keys(r.body)){if(safe.includes(k))r.user[k]=r.body[k]}s.json(r.user)})"),
    ("javascript","function sN(o,p,v){const ps=p.split(\".\");let c=o;for(let i=0;i<ps.length-1;i++){c=c[ps[i]]}c[ps[ps.length-1]]=v}","function sN(o,p,v){const ps=p.split(\".\");if(ps.some(x=>x==\"__proto__\"||x==\"constructor\"))return;let c=o;for(let i=0;i<ps.length-1;i++){c=c[ps[i]]}c[ps[ps.length-1]]=v}"),
    ("web","<script>const p=new URLSearchParams(location.s);const c={};for(const[k,v]of p){c[k]=v}</script>","<script>const p=new URLSearchParams(location.s);const c={};for(const[k,v]of p){if(k==\"__proto__\"||k==\"constructor\")continue;c[k]=v}</script>"),
    # CORS
    ("python","@app.after_request\\ndef cors(r):\\n    r.headers[\"Access-Control-Allow-Origin\"]=\"*\"\\n    return r","@app.after_request\\ndef cors(r):\\n    o=request.headers.get(\"Origin\")\\n    if o in [\"https://x.com\",\"https://app.x.com\"]:\\n        r.headers[\"Access-Control-Allow-Origin\"]=o\\n    return r"),
    ("python","from flask_cors import CORS\\nCORS(app)","from flask_cors import CORS\\nCORS(app,origins=[\"https://x.com\"],supports_credentials=True)"),
    ("javascript","app.use((r,s,n)=>{s.header(\"Access-Control-Allow-Origin\",\"*\");s.header(\"Access-Control-Allow-Credentials\",\"true\");n()})","const cors=require(\"cors\");app.use(cors({origin:\"https://x.com\",credentials:true}))"),
    ("javascript","app.use((r,s,n)=>{s.header(\"Access-Control-Allow-Origin\",r.headers.origin);s.header(\"Access-Control-Allow-Credentials\",\"true\");n()})","app.use((r,s,n)=>{const o=r.headers.origin;if([\"https://x.com\",\"https://app.x.com\"].includes(o)){s.header(\"Access-Control-Allow-Origin\",o);s.header(\"Access-Control-Allow-Credentials\",\"true\")}n()})"),
    ("java","@Configuration class C implements WebMvcConfigurer{@Override void addCorsMappings(CorsRegistry r){r.addMapping(\"/**\").allowedOrigins(\"*\")}}","@Configuration class C implements WebMvcConfigurer{@Override void addCorsMappings(CorsRegistry r){r.addMapping(\"/api/**\").allowedOrigins(\"https://x.com\")}}"),
    ("go","func cors(n http.Handler)http.Handler{return http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){w.Header().Set(\"Access-Control-Allow-Origin\",\"*\");w.Header().Set(\"Access-Control-Allow-Credentials\",\"true\");n.ServeHTTP(w,r)})}","func cors(n http.Handler)http.Handler{return http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){o:=r.Header.Get(\"Origin\");if o==\"https://x.com\"||o==\"https://app.x.com\"{w.Header().Set(\"Access-Control-Allow-Origin\",o)}w.Header().Set(\"Access-Control-Allow-Credentials\",\"true\");n.ServeHTTP(w,r)})}"),
    ("web","<?php header(\"Access-Control-Allow-Origin: *\");header(\"Access-Control-Allow-Credentials: true\");?>","<?php $o=$_SERVER[\"HTTP_ORIGIN\"]??\"\";$a=[\"https://x.com\"];if(in_array($o,$a)){header(\"Access-Control-Allow-Origin: $o\");header(\"Access-Control-Allow-Credentials: true\")}?>"),
    # Hardcoded Credentials
    ("python","DB_PASS=\"sifre123\";DB_USER=\"admin\"\\ndef c():return pymysql.connect(user=DB_USER,password=DB_PASS)","import os\\ndef c():return pymysql.connect(user=os.environ[\"DB_USER\"],password=os.environ[\"DB_PASS\"])"),
    ("python","API_KEY=\"sk-abc123\"\\ndef call():return requests.post(\"https://api.x.com\",headers={\"Authorization\":f\"Bearer {API_KEY}\"})","import os\\ndef call():k=os.environ.get(\"API_KEY\");if not k:raise ValueError();return requests.post(\"https://api.x.com\",headers={\"Authorization\":f\"Bearer {k}\"})"),
    ("javascript","const AWS_KEY=\"AKIA123\";const AWS_SEC=\"abc123\"\\nconst s3=new AWS.S3({accessKeyId:AWS_KEY,secretAccessKey:AWS_SEC})","const s3=new AWS.S3({accessKeyId:process.env.AWS_KEY,secretAccessKey:process.env.AWS_SEC})"),
    ("javascript","const SECRET=\"mykey123\"\\nfunction t(u){return jwt.sign(u,SECRET,{expiresIn:\"1h\"})}","function t(u){const s=process.env.JWT_SECRET;if(!s)throw Error();return jwt.sign(u,s,{expiresIn:\"1h\"})}"),
    ("java","class DBConfig{static final String URL=\"jdbc:mysql://localhost/db\";static final String U=\"root\";static final String P=\"pass\";Connection get(){return DriverManager.getConnection(URL,U,P)}}","class DBConfig{Connection get(){return DriverManager.getConnection(System.getenv(\"DB_URL\"),System.getenv(\"DB_USER\"),System.getenv(\"DB_PASS\"))}}"),
    ("go","const(dbUser=\"postgres\";dbPass=\"pass123\")\\nfunc open()(*sql.DB,error){return sql.Open(\"postgres\",fmt.Sprintf(\"user=%s password=%s\",dbUser,dbPass))}","func open()(*sql.DB,error){return sql.Open(\"postgres\",fmt.Sprintf(\"user=%s password=%s\",os.Getenv(\"DB_USER\"),os.Getenv(\"DB_PASS\")))}"),
    ("go","const token=\"ghp_xxx\"\\nfunc repos(){req,_:=http.NewRequest(\"GET\",\"https://api.github.com/user/repos\",nil);req.Header.Set(\"Authorization\",\"token \"+token)}","func repos(){t:=os.Getenv(\"GITHUB_TOKEN\");if t==\"\"{log.Fatal(\"no token\")}req,_:=http.NewRequest(\"GET\",\"https://api.github.com/user/repos\",nil);req.Header.Set(\"Authorization\",\"token \"+t)}"),
    ("web","<?php $db_p=\"root\";$db_u=\"root\";$pdo=new PDO(\"mysql:host=localhost;dbname=t\",$db_u,$db_p);?>","<?php $db_u=getenv(\"DB_USER\");$db_p=getenv(\"DB_PASS\");if(!$db_u||!$db_p)die();$pdo=new PDO(\"mysql:host=localhost;dbname=t\",$db_u,$db_p);?>"),
    # Open Redirect
    ("python","@app.route(\"/r\")\\ndef r():return redirect(request.args.get(\"next\",\"/\"))","ALLOWED=[\"x.com\",\"app.x.com\"]\\n@app.route(\"/r\")\\ndef r():\\n    t=request.args.get(\"next\",\"/\")\\n    p=urlparse(t)\\n    if p.netloc and p.netloc not in ALLOWED:return \"no\",400\\n    return redirect(t)"),
    ("python","@app.route(\"/go\")\\ndef go():return redirect(request.args.get(\"url\"))","@app.route(\"/go\")\\ndef go():\\n    u=request.args.get(\"url\")\\n    p=urlparse(u)\\n    if not p.netloc:return redirect(u)\\n    if p.netloc!=\"x.com\":return \"no\",400\\n    return redirect(u)"),
    ("javascript","app.get(\"/r\",(r,s)=>{s.redirect(r.query.u)})","app.get(\"/r\",(r,s)=>{const u=r.query.u;if(![\"https://x.com\",\"https://app.x.com\"].includes(u))return s.status(400).send(\"no\");s.redirect(u)})"),
    ("javascript","app.get(\"/out\",(r,s)=>{s.writeHead(302,{Location:r.query.to});s.end()})","app.get(\"/out\",(r,s)=>{try{const p=new URL(r.query.to);if(p.hostname!==\"x.com\")return s.status(400).send(\"no\");s.redirect(r.query.to)}catch{s.status(400).send(\"invalid\")}})"),
    ("java","@GetMapping(\"/r\")String r(@RequestParam String u){return \"redirect:\"+u}","@GetMapping(\"/r\")String r(@RequestParam String u){List<String>a=Arrays.asList(\"https://x.com\");if(!a.contains(u))return\"redirect:/\";return\"redirect:\"+u}"),
    ("go","func r(w http.ResponseWriter,r*http.Request){http.Redirect(w,r,r.URL.Query().Get(\"u\"),302)}","func r(w http.ResponseWriter,r*http.Request){u:=r.URL.Query().Get(\"u\");p,_:=url.Parse(u);if p.Host!=\"\"&&p.Host!=\"x.com\"{http.Error(w,\"no\",400);return}http.Redirect(w,r,u,302)}"),
    ("web","<?php header(\"Location: \".$_GET[\"u\"]);exit;?>","<?php $u=$_GET[\"u\"];$p=parse_url($u);if(isset($p[\"host\"])&&$p[\"host\"]!=\"x.com\"){$u=\"/\"}header(\"Location: $u\");exit;?>"),
    # Security Headers
    ("python","@app.route(\"/\")\\ndef i():return \"Merhaba\"","@app.after_request\\ndef h(r):\\n    r.headers[\"X-Content-Type-Options\"]=\"nosniff\"\\n    r.headers[\"X-Frame-Options\"]=\"DENY\"\\n    r.headers[\"Strict-Transport-Security\"]=\"max-age=31536000\"\\n    return r\\n@app.route(\"/\")\\ndef i():return \"Merhaba\""),
    ("python","from flask import Flask\\napp=Flask(__name__)\\n@app.route(\"/api\")\\ndef api():return jsonify({\"s\":\"ok\"})","from flask_talisman import Talisman\\nTalisman(app,content_security_policy=None,force_https=True)\\n@app.route(\"/api\")\\ndef api():return jsonify({\"s\":\"ok\"})"),
    ("javascript","const app=require(\"express\")();app.get(\"/\",(r,s)=>s.send(\"Hello\"))","const helmet=require(\"helmet\");const app=require(\"express\")();app.use(helmet());app.get(\"/\",(r,s)=>s.send(\"Hello\"))"),
    ("javascript","const app=require(\"express\")();app.get(\"/d\",(r,s)=>s.json({s:\"data\"}))","const helmet=require(\"helmet\");app.use(helmet({contentSecurityPolicy:{directives:{defaultSrc:[\"'self'\"]}}}))"),
    ("java","@RestController class H{@GetMapping(\"/h\")String h(){return\"Merhaba\"}}","@Configuration @EnableWebSecurity class S extends WebSecurityConfigurerAdapter{@Override void configure(HttpSecurity h){h.headers().xssProtection().and().contentTypeOptions().and().frameOptions().deny()}}"),
    ("go","func main(){http.HandleFunc(\"/\",func(w http.ResponseWriter,r*http.Request){w.Write([]byte(\"Merhaba\"))});http.ListenAndServe(\":8080\",nil)}","func h(next http.Handler)http.Handler{return http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){w.Header().Set(\"X-Content-Type-Options\",\"nosniff\");w.Header().Set(\"X-Frame-Options\",\"DENY\");next.ServeHTTP(w,r)})}\\nfunc main(){m:=http.NewServeMux();m.Handle(\"/\",h(http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){w.Write([]byte(\"Merhaba\"))})));http.ListenAndServe(\":8080\",m)}"),
    ("web","<!DOCTYPE html><html><head><title>S</title></head><body><h1>Merhaba</h1></body></html>","<!DOCTYPE html><html><head><meta http-equiv=\"X-Content-Type-Options\" content=\"nosniff\"><meta http-equiv=\"X-Frame-Options\" content=\"DENY\"><title>S</title></head><body><h1>Merhaba</h1></body></html>"),
    # Insecure Randomness
    ("python","import random\\ndef token():return ''.join(random.choices('abcdef0123456789',k=32))","import secrets\\ndef token():return secrets.token_hex(16)"),
    ("python","import random\\ndef pwd():return ''.join(random.choice(string.ascii_letters+string.digits)for _ in range(12))","import secrets\\ndef pwd():return ''.join(secrets.choice(string.ascii_letters+string.digits)for _ in range(12))"),
    ("javascript","function tok(){return Math.random().toString(36).substring(2)}","function tok(){return crypto.randomBytes(32).toString('hex')}"),
    ("java","String tok(){Random r=new Random();return Long.toHexString(r.nextLong())}","String tok(){SecureRandom s=new SecureRandom();byte[]b=new byte[32];s.nextBytes(b);return bytesToHex(b)}"),
    ("go","import \"math/rand\"\\nfunc Tok()string{b:=make([]byte,16);rand.Read(b);return hex.EncodeToString(b)}","import \"crypto/rand\"\\nfunc Tok()string{b:=make([]byte,16);rand.Read(b);return hex.EncodeToString(b)}"),
    # Weak Password Hashing
    ("python","import hashlib\\ndef h(p):return hashlib.sha256(p.encode()).hexdigest()","import bcrypt\\ndef h(p):return bcrypt.hashpw(p.encode(),bcrypt.gensalt())"),
    ("python","def h(p):return hashlib.md5(p.encode()).hexdigest()","from werkzeug.security import generate_password_hash\\ndef h(p):return generate_password_hash(p)"),
    ("javascript","function h(p){return crypto.createHash('md5').update(p).digest('hex')}","async function h(p){return await bcrypt.hash(p,12)}"),
    ("javascript","function h(p){return crypto.createHash('sha256').update(p).digest('hex')}","async function h(p){const s=await bcrypt.genSalt(12);return await bcrypt.hash(p,s)}"),
    ("java","String h(String p)throws Exception{MessageDigest md=MessageDigest.getInstance(\"MD5\");return bytesToHex(md.digest(p.getBytes()))}","String h(String p){return BCrypt.hashpw(p,BCrypt.gensalt(12))}"),
    ("go","func h(p string)string{h:=sha256.Sum256([]byte(p));return hex.EncodeToString(h[:])}","import \"golang.org/x/crypto/bcrypt\"\\nfunc h(p string)(string,error){b,err:=bcrypt.GenerateFromPassword([]byte(p),12);return string(b),err}"),
    ("web","<?php $h=md5($p);$db->prepare(\"INSERT INTO users(p)VALUES(?)\")->execute([$h]);?>","<?php $h=password_hash($p,PASSWORD_BCRYPT,[\"cost\"=>12]);$db->prepare(\"INSERT INTO users(p)VALUES(?)\")->execute([$h]);?>"),
    # JWT Issues
    ("python","def verify(t):return jwt.decode(t,options={\"verify_signature\":False})","def verify(t):return jwt.decode(t,\"secret\",algorithms=[\"HS256\"])"),
    ("python","def create(uid):return jwt.encode({\"uid\":uid},\"\",algorithm=\"none\")","def create(uid):return jwt.encode({\"uid\":uid},\"supersecret\",algorithm=\"HS256\")"),
    ("javascript","const t=jwt.sign({u:id},'',{algorithm:'none'})","const t=jwt.sign({u:id},process.env.JWT_SECRET,{algorithm:'HS256'})"),
    ("javascript","const d=jwt.decode(t)","const d=jwt.verify(t,process.env.JWT_SECRET)"),
    ("javascript","function auth(r,s,n){try{r.user=jwt.verify(r.headers.a,'12345');n()}catch{s.status(401).send('no')}}","function auth(r,s,n){try{r.user=jwt.verify(r.headers.a,process.env.JWT_SECRET);n()}catch{s.status(401).send('no')}}"),
    ("java","String create(String uid){return Jwts.builder().setSubject(uid).signWith(SignatureAlgorithm.NONE).compact()}","String create(String uid){return Jwts.builder().setSubject(uid).signWith(SignatureAlgorithm.HS256,key).compact()}"),
    ("java","Claims parse(String t){return Jwts.parser().parseClaimsJwt(t).getBody()}","Claims parse(String t){return Jwts.parser().setSigningKey(key).parseClaimsJws(t).getBody()}"),
    ("go","func parse(t string)(*Claims,error){tok,_:=jwt.Parse(t,nil);return tok.Claims.(*Claims),nil}","func parse(t string)(*Claims,error){tok,err:=jwt.Parse(t,func(t*jwt.Token)(interface{},error){return[]byte(os.Getenv(\"JWT_SECRET\")),nil});if err!=nil{return nil,err}return tok.Claims.(*Claims),nil}"),
    ("go","func create(uid string)string{t:=jwt.New(jwt.SigningMethodNone);t.Claims.(jwt.MapClaims)[\"u\"]=uid;s,_:=t.SignedString(jwt.UnsafeAllowNoneSignatureType);return s}","func create(uid string)(string,error){t:=jwt.NewWithClaims(jwt.SigningMethodHS256,jwt.MapClaims{\"u\":uid,\"exp\":time.Now().Add(time.Hour).Unix()});return t.SignedString([]byte(os.Getenv(\"JWT_SECRET\")))}"),
    ("web","<?php $p=[\"uid\"=>1];$j=JWT::encode($p,'','none');?>","<?php $p=[\"uid\"=>1,\"exp\"=>time()+3600];$j=JWT::encode($p,getenv('JWT_SECRET'),'HS256');?>"),
    # Info Disclosure
    ("python","@app.route(\"/e\")\\ndef e():raise Exception(\"hata\")\\n@app.errorhandler(Exception)\\ndef h(e):return str(e),500","@app.errorhandler(Exception)\\ndef h(e):\\n    app.logger.error(str(e))\\n    return \"hata\",500"),
    ("python","app.config[\"DEBUG\"]=True","app.config[\"DEBUG\"]=os.environ.get(\"FLASK_ENV\")==\"development\""),
    ("javascript","app.use((e,r,s,n)=>{s.status(500).send(e.stack)})","app.use((e,r,s,n)=>{console.error(e.stack);s.status(500).send(\"Internal error\")})"),
    ("javascript","app.get(\"/cfg\",(r,s)=>{s.json({db:process.env.DB_URL,secret:process.env.SECRET})})","app.get(\"/cfg\",(r,s)=>{s.json({env:process.env.NODE_ENV})})"),
    ("java","@GetMapping(\"/debug\")String debug(){return System.getenv().toString()}","@Profile(\"dev\")@GetMapping(\"/debug\")String debug(){return \"dev mode\"}"),
    ("go","func d(w http.ResponseWriter,r*http.Request){w.Write([]byte(fmt.Sprintf(\"DB:%s\",os.Getenv(\"DB_URL\"))))}","func d(w http.ResponseWriter,r*http.Request){if os.Getenv(\"APP_ENV\")!=\"dev\"{http.Error(w,\"no\",403);return}w.Write([]byte(\"debug\"))}"),
    ("python","@app.route(\"/health\")\\ndef h():return open(\"/etc/passwd\").read()","@app.route(\"/health\")\\ndef h():return jsonify({\"status\":\"healthy\"})"),
    ("web","<?php phpinfo();?>","<?php if($_SERVER[\"REMOTE_ADDR\"]!==\"127.0.0.1\")die();phpinfo();?>"),
]
for l,bad,good in pairs_sec3:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

print(f"After sec3: {len(D)}")

# ===== Add more refactoring pairs =====
pairs_ref2 = [
    # More Python refactoring
    ("python","def price(amt,tax):\\n    t=amt*tax\\n    return amt+t","def price(amt,tax):\\n    return amt*(1+tax)"),
    ("python","if status==1: return \"active\"\\nelif status==2: return \"inactive\"\\nelif status==3: return \"pending\"\\nelse: return \"unknown\"","STATUS={1:\"active\",2:\"inactive\",3:\"pending\"}\\ndef get_status(s):return STATUS.get(s,\"unknown\")"),
    ("python","def process(order):\\n    if order.is_paid:\\n        if order.is_shipped:\\n            if order.is_delivered:\\n                return \"done\"\\n            else: return \"in_transit\"\\n        else: return \"pending_shipment\"\\n    else: return \"awaiting_payment\"","def process(order):\\n    if not order.is_paid: return \"awaiting_payment\"\\n    if not order.is_shipped: return \"pending_shipment\"\\n    if not order.is_delivered: return \"in_transit\"\\n    return \"done\""),
    ("python","def calc_discount(customer,items):\\n    discount=0\\n    if customer.is_premium:\\n        discount=0.2\\n    else:\\n        if len(items)>5:\\n            discount=0.1\\n        else:\\n            discount=0\\n    return discount","def calc_discount(customer,items):\\n    if customer.is_premium:return 0.2\\n    if len(items)>5:return 0.1\\n    return 0"),
    ("python","def send_email(addr,subj,body):\\n    msg=f\"Subject: {subj}\\\\nTo: {addr}\\\\n{body}\"\\n    smtp.send(msg)","def send_email(addr,subj,body):\\n    msg=EmailMessage()\\n    msg[\"Subject\"]=subj\\n    msg[\"To\"]=addr\\n    msg.set_content(body)\\n    smtp.send_message(msg)"),
    ("python","result=[]\\nfor student in students:\\n    if student.grade>=60:\\n        result.append({\"name\":student.name,\"grade\":student.grade})","result=[{\"name\":s.name,\"grade\":s.grade}for s in students if s.grade>=60]"),
    ("python","def get_full_name(user):\\n    first=user.get(\"first_name\",\"\")\\n    last=user.get(\"last_name\",\"\")\\n    return f\"{first} {last}\".strip()","def get_full_name(user):\\n    return f\"{user.get('first_name','')} {user.get('last_name','')}\".strip()"),
    ("python","class MathOps:\\n    @staticmethod\\n    def add(a,b):return a+b\\n    @staticmethod\\n    def sub(a,b):return a-b","# module-level functions\\ndef add(a,b):return a+b\\ndef sub(a,b):return a-b"),
    ("python","def validate(data):\\n    errors=[]\\n    if len(data.get(\"name\",\"\"))<2:\\n        errors.append(\"name too short\")\\n    if len(data.get(\"email\",\"\"))<5:\\n        errors.append(\"email too short\")\\n    if data.get(\"age\",0)<18:\\n        errors.append(\"too young\")\\n    return errors","VALIDATORS=[\\n    (\"name\",lambda n:len(n)>=2 or \"name too short\"),\\n    (\"email\",lambda e:len(e)>=5 or \"email too short\"),\\n    (\"age\",lambda a:a>=18 or \"too young\"),\\n]\\ndef validate(data):\\n    return [msg for field,fn in VALIDATORS if (msg:=fn(data.get(field,0)))]"),
    ("python","def get_config():\\n    import json\\n    with open(\"config.json\") as f:\\n        return json.load(f)","import json\\nCONFIG=None\\ndef get_config():\\n    global CONFIG\\n    if CONFIG is None:\\n        with open(\"config.json\") as f:\\n            CONFIG=json.load(f)\\n    return CONFIG"),
    ("python","def format_name(first,last,middle=None):\\n    if middle:\\n        return f\"{first} {middle} {last}\"\\n    return f\"{first} {last}\"","def format_name(first,last,middle=\"\"):\\n    parts=[first,middle,last]\\n    return \" \".join(p for p in parts if p)"),
    ("python","def calculate(price,qty,tax,discount):\\n    sub=price*qty\\n    taxed=sub*(1+tax)\\n    total=taxed*(1-discount)\\n    return total","def calculate(price,qty,tax=0,discount=0):\\n    return price*qty*(1+tax)*(1-discount)"),
    ("python","class User:\\n    def __init__(self,n,e):\\n        self.n=n\\n        self.e=e\\n    def get_n(self):return self.n\\n    def get_e(self):return self.e","class User:\\n    def __init__(self,name,email):\\n        self.name=name\\n        self.email=email\\n    @property\\n    def name(self):return self._name\\n    @name.setter\\n    def name(self,v):self._name=v"),
    ("python","def fib(n):\\n    if n<=1:return n\\n    return fib(n-1)+fib(n-2)","from functools import lru_cache\\n@lru_cache\\ndef fib(n):\\n    if n<=1:return n\\n    return fib(n-1)+fib(n-2)"),
    ("python","def load_users():\\n    return pd.read_csv(\"users.csv\").to_dict(\"records\")","def load_users():\\n    import csv\\n    with open(\"users.csv\") as f:\\n        return list(csv.DictReader(f))"),
    ("python","for key in dict.keys(): print(key,dict[key])","for key,val in dict.items(): print(key,val)"),
    ("python","try:\\n    do_something()\\nexcept: pass","from contextlib import suppress\\nwith suppress(Exception): do_something()"),
    ("python","def save_user(user):\\n    db=get_db()\\n    db.execute(\"INSERT INTO users(name)VALUES(?)\",(user.name,))\\n    db.commit()","def save_user(user):\\n    with get_db() as db:\\n        db.execute(\"INSERT INTO users(name)VALUES(?)\",(user.name,))"),
    ("python","s=set()\\nfor x in items:\\n    s.add(x)","s=set(items)"),
    ("python","d={}\\nfor k,v in pairs:\\n    d[k]=v","d=dict(pairs)"),
    # More JavaScript refactoring
    ("javascript","function sum(a,b,c,d){return a+b+c+d}","function sum(...n){return n.reduce((a,b)=>a+b,0)}"),
    ("javascript","const x=[];for(let i=0;i<10;i++){if(i%2===0)x.push(i)}","const x=[...Array(10).keys()].filter(i=>i%2===0)"),
    ("javascript","function getById(id){return document.querySelector('#')+id}","function getById(id){return document.getElementById(id)}"),
    ("javascript","const result=Math.max.apply(null,arr)","const result=Math.max(...arr)"),
    ("javascript","function greet(name){if(!name){name='Guest'}return 'Hello '+name}","function greet(name='Guest'){return `Hello ${name}`}"),
    ("javascript","const obj={a:1,b:2,c:3};const keys=Object.keys(obj).map(k=>obj[k])","const obj={a:1,b:2,c:3};const values=Object.values(obj)"),
    ("javascript","const evens=[];odds=[];for(let n of nums){if(n%2===0)evens.push(n);else odds.push(n)}","const evens=nums.filter(n=>n%2===0);const odds=nums.filter(n=>n%2===1)"),
    ("javascript","if(window.location.href.includes('admin'))","if(window.location.pathname.startsWith('/admin'))"),
    ("javascript","const start=Date.now();doWork();const end=Date.now();console.log(end-start)","console.time('work');doWork();console.timeEnd('work')"),
    ("javascript","const data=JSON.parse(JSON.stringify(obj))","const data=structuredClone(obj)"),
    ("javascript","function makeRequest(url,cb){fetch(url).then(r=>r.json()).then(d=>cb(d)).catch(e=>console.log(e))}","async function makeRequest(url){try{const r=await fetch(url);return await r.json()}catch(e){console.error(e)}}"),
    ("javascript","setTimeout(function(){alert('done')},1000)","setTimeout(()=>alert('done'),1000)"),
    ("javascript","if(arr.indexOf(5)!==-1)","if(arr.includes(5))"),
    ("javascript","const t=document.createTextNode('Hello');document.body.appendChild(t)","document.body.append('Hello')"),
    ("javascript","const h=window.location.href;const p=window.location.pathname","const{hostname:href,pathname}=window.location"),
    # More Java refactoring
    ("java","public boolean isActive(){if(status==1){return true;}else{return false;}}","public boolean isActive(){return status==1;}"),
    ("java","String s=new String(\"hello\")","String s=\"hello\""),
    ("java","Map<String,String>m=new HashMap<String,String>()","var m=new HashMap<String,String>()"),
    ("java","if(list.size()>0)","if(!list.isEmpty())"),
    ("java","for(int i=0;i<list.size();i++){System.out.println(list.get(i));}","list.forEach(System.out::println)"),
    ("java","List<Integer>nums=Arrays.asList(1,2,3,4,5)","var nums=List.of(1,2,3,4,5)"),
    ("java","public String getFullName(){return this.firstName+\" \"+this.lastName;}","public String getFullName(){return String.format(\"%s %s\",firstName,lastName);}"),
    ("java","String[]arr=new String[]{\"a\",\"b\",\"c\"}","String[]arr={\"a\",\"b\",\"c\"}"),
    ("java","public void log(String msg){System.out.println(java.time.LocalDateTime.now()+\": \"+msg);}","private static final Logger LOG=Logger.getLogger(getClass().getName());\\npublic void log(String msg){LOG.info(msg);}"),
    ("java","if(obj!=null){obj.call();}","if(Objects.nonNull(obj)){obj.call();}"),
    ("java","int sum=0;for(int n:nums){sum+=n;}","int sum=nums.stream().mapToInt(Integer::intValue).sum()"),
    ("java","public void connect()throws Exception{Class.forName(\"com.mysql.Driver\");}","// Driver auto-registered in modern JDBC"),
    ("java","File f=new File(\"/tmp/data.txt\");Scanner s=new Scanner(f);while(s.hasNext()){System.out.println(s.nextLine());}s.close();","try(var s=new Scanner(Path.of(\"/tmp/data.txt\"))){s.useDelimiter(\"\\n\").forEachRemaining(System.out::println);}"),
    ("java","List<String>upper=new ArrayList<>();for(String s:list){upper.add(s.toUpperCase());}","var upper=list.stream().map(String::toUpperCase).toList()"),
    ("java","Collections.sort(list)","list.sort(null)"),
    # More Go refactoring
    ("go","func isEven(n int)bool{if n%2==0{return true}return false}","func isEven(n int)bool{return n%2==0}"),
    ("go","type Person struct{name string;age int}","type Person struct{\n\tName string\n\tAge  int\n}"),
    ("go","func f(x int)int{var y int;y=x*2;return y}","func f(x int)int{return x*2}"),
    ("go","for i:=0;i<5;i++{defer fmt.Println(i)}","for i:=range 5{defer func(i int){fmt.Println(i)}(i)}"),
    ("go","m:=make(map[string]int);m[\"a\"]=1;m[\"b\"]=2","m:=map[string]int{\"a\":1,\"b\":2}"),
    ("go","s:=\"\";for _,n:=range names{s+=n+\",\"};s=strings.TrimSuffix(s,\",\")","s:=strings.Join(names,\",\")"),
    ("go","if len(arr)>0{}","if len(arr)!=0{}"),
    ("go","t:=time.Now().UnixNano()/1e6","t:=time.Now().UnixMilli()"),
    ("go","result:=make([]int,0);for _,v:=range input{result=append(result,v*2)}","result:=lo.Map(input,func(v int,_ int)int{return v*2})"),
    ("go","func main(){http.HandleFunc(\"/\",handler);http.ListenAndServe(\":8080\",nil)}","func main(){mux:=http.NewServeMux();mux.HandleFunc(\"/\",handler);http.ListenAndServe(\":8080\",mux)}"),
    ("go","if s==\"\"{return true}else{return false}","return s==\"\""),
    ("go","var result=0;for _,n:=range numbers{result+=n};return result","func sum(numbers []int)int{result:=0;for _,n:=range numbers{result+=n};return result}"),
    ("go","type Handler struct{};func(h*Handler)ServeHTTP(http.ResponseWriter,*http.Request){}","// Use http.HandlerFunc instead of struct for simple handlers"),
    ("go","data:=[]byte(\"hello\")","data:=[]byte(\"hello\")"),
    ("go","if strings.Contains(s,\"x\")==true{}","if strings.Contains(s,\"x\"){}"),
    # More TypeScript refactoring
    ("typescript","function f(x:number):number{if(x>0)return x;else return 0}","function f(x:number):number{return Math.max(0,x)}"),
    ("typescript","const myVar:number=100","const MY_VAR=100"),
    ("typescript","function f(arr:Array<number>):number{return arr.length}","function f(arr:number[]):number{return arr.length}"),
    ("typescript","import * as React from 'react'","import React from 'react'"),
    ("typescript","if(arr.find(x=>x===5)!==undefined)","if(arr.includes(5))"),
    ("typescript","let x:number|undefined;if(condition)x=5;else x=0","const x=condition?5:0"),
    ("typescript","type Props={name:string;age?:number};function C(props:Props){return props.name}","interface Props{name:string;age?:number};function C({name}:Props){return name}"),
    ("typescript","const result=items.reduce((acc,item)=>acc+item.value,0)","const result=items.reduce((sum,{value})=>sum+value,0)"),
    ("typescript","function f(x:any){console.log((x as string).length)}","function f(x:string){console.log(x.length)}"),
    ("typescript","document.querySelector('.btn')!.addEventListener('click',()=>{})","document.querySelector<HTMLButtonElement>('.btn')!.addEventListener('click',()=>{})"),
    ("typescript","const promise:Promise<number>=fetch('/api').then(r=>r.json())","const promise=fetch('/api').then(r=>r.json() as Promise<number>)"),
    ("typescript","interface User{id:number;name:string;email:string;password:string}","interface User{id:number;name:string;email:string} // Omit password"),
    ("typescript","type Status='active'|'inactive'|'pending'","const enum Status{ACTIVE='active',INACTIVE='inactive',PENDING='pending'}"),
    ("typescript","const data=response.data as any","const data=response.data as MyResponseType"),
    ("typescript","if(obj&&obj.prop&&obj.prop.value){}","if(obj?.prop?.value){}"),
]
for l,bad,good in pairs_ref2:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)

print(f"After ref2: {len(D)}")

pairs_sec4 = [
    # Broken Auth / Session Fixation
    ("python","@app.route(\"/login\",methods=[\"POST\"])\\ndef login():\\n    u=authenticate(request.form[\"u\"],request.form[\"p\"])\\n    session[\"user\"]=u\\n    return \"ok\"","@app.route(\"/login\",methods=[\"POST\"])\\ndef login():\\n    u=authenticate(request.form[\"u\"],request.form[\"p\"])\\n    session.clear()\\n    session[\"user\"]=u\\n    return \"ok\""),
    ("javascript","app.post(\"/login\",(r,s)=>{const u=users.find(x=>x.u===r.body.u&&x.p===r.body.p);r.session.user=u;s.redirect(\"/\")})","app.post(\"/login\",(r,s)=>{const u=users.find(x=>x.u===r.body.u);if(!u||!bcrypt.compareSync(r.body.p,u.p))return s.status(401).send(\"no\");r.session.regenerate(()=>{r.session.userId=u.id;s.redirect(\"/\")})})"),
    ("java","@PostMapping(\"/login\")String login(@RequestParam String u,@RequestParam String p,HttpSession s){User user=userService.auth(u,p);s.setAttribute(\"user\",user);return\"redirect:/\"}","@PostMapping(\"/login\")String login(@RequestParam String u,@RequestParam String p,HttpServletRequest r){User user=userService.auth(u,p);HttpSession s=r.getSession(false);if(s!=null)s.invalidate();s=r.getSession(true);s.setAttribute(\"user\",user);return\"redirect:/\"}"),
    ("go","func login(w http.ResponseWriter,r*http.Request){u:=auth(r.FormValue(\"u\"),r.FormValue(\"p\"));s,_:=store.Get(r,\"s\");s.Values[\"u\"]=u;s.Save(r,w);http.Redirect(w,r,\"/\",302)}","func login(w http.ResponseWriter,r*http.Request){u:=auth(r.FormValue(\"u\"),r.FormValue(\"p\"));s,_:=store.New(r,\"s\");s.Values[\"u\"]=u;s.Save(r,w);http.Redirect(w,r,\"/\",302)}"),
    ("javascript","app.post(\"/login\",(r,s)=>{db.get(\"SELECT * FROM users WHERE username=?\",[r.body.u],(e,u)=>{if(u&&u.password===r.body.p){r.session.u=u.id;s.redirect(\"/d\")}else{s.send(\"no\")}})})","app.post(\"/login\",(r,s)=>{db.get(\"SELECT * FROM users WHERE username=?\",[r.body.u],async(e,u)=>{if(u&&await bcrypt.compare(r.body.p,u.p)){r.session.u=u.id;s.redirect(\"/d\")}else{s.status(401).send(\"no\")}})})"),
    ("python","def login():\\n    if request.form[\"u\"]==\"admin\"and request.form[\"p\"]==\"admin123\":\\n        session[\"admin\"]=True\\n        return redirect(\"/admin\")","def login():\\n    u=db.execute(\"SELECT * FROM users WHERE username=?\",(request.form[\"u\"],)).fetchone()\\n    if u and bcrypt.checkpw(request.form[\"p\"].encode(),u[\"p\"]):\\n        session[\"uid\"]=u[\"id\"]\\n        session[\"is_admin\"]=u[\"is_admin\"]\\n        return redirect(\"/admin\" if u[\"is_admin\"]else \"/\")"),
    # Host Header Injection
    ("python","@app.route(\"/reset\")\\ndef reset():\\n    t=token()\\n    l=f\"https://{request.host}/reset/{t}\"\\n    send_email(l)\\n    return \"ok\"","@app.route(\"/reset\")\\ndef reset():\\n    t=token()\\n    h=request.headers.get(\"Host\",\"\")\\n    if h not in [\"x.com\",\"www.x.com\"]:h=\"x.com\"\\n    l=f\"https://{h}/reset/{t}\"\\n    send_email(l)\\n    return \"ok\""),
    ("javascript","app.post(\"/reset\",(r,s)=>{const t=crypto.randomBytes(20).toString('hex');sendEmail(r.body.e,`http://${r.headers.host}/reset/${t}`);s.send('ok')})","app.post(\"/reset\",(r,s)=>{const t=crypto.randomBytes(20).toString('hex');const h=r.headers.host;if(!['x.com','www.x.com'].includes(h))return s.status(400).send('no');sendEmail(r.body.e,`https://${h}/reset/${t}`);s.send('ok')})"),
    ("go","func reset(w http.ResponseWriter,r*http.Request){t:=genToken();l:=fmt.Sprintf(\"http://%s/reset/%s\",r.Host,t);sendEmail(r.FormValue(\"e\"),l);w.Write([]byte(\"ok\"))}","func reset(w http.ResponseWriter,r*http.Request){t:=genToken();h:=r.Host;if h!=\"x.com\"&&h!=\"www.x.com\"{h=\"x.com\"}l:=fmt.Sprintf(\"https://%s/reset/%s\",h,t);sendEmail(r.FormValue(\"e\"),l);w.Write([]byte(\"ok\"))}"),
    # Clickjacking
    ("python","@app.route(\"/\")\\ndef i():return render_template(\"i.html\")","@app.after_request\\ndef h(r):r.headers[\"X-Frame-Options\"]=\"DENY\";return r"),
    ("javascript","app.get(\"/\",(r,s)=>s.send('<h1>Merhaba</h1>'))","app.use((r,s,n)=>{s.setHeader('X-Frame-Options','DENY');n()});app.get(\"/\",(r,s)=>s.send('<h1>Merhaba</h1>'))"),
    ("go","func main(){http.HandleFunc(\"/\",func(w http.ResponseWriter,r*http.Request){w.Write([]byte(\"<h1>Site</h1>\"))});http.ListenAndServe(\":8080\",nil)}","func click(n http.Handler)http.Handler{return http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){w.Header().Set(\"X-Frame-Options\",\"DENY\");n.ServeHTTP(w,r)})}\\nfunc main(){m:=http.NewServeMux();m.Handle(\"/\",click(http.HandlerFunc(func(w http.ResponseWriter,r*http.Request){w.Write([]byte(\"<h1>Site</h1>\"))})));http.ListenAndServe(\":8080\",m)}"),
    # NoSQL Injection
    ("javascript","app.post(\"/login\",async(r,s)=>{const{u,p}=r.body;const user=await db.collection('users').findOne({username:u,password:p});if(user)s.json({ok:1});else s.status(401).json({ok:0})})","app.post(\"/login\",async(r,s)=>{const{u,p}=r.body;if(typeof u!='string'||typeof p!='string')return s.status(400).json({e:\"no\"});const user=await db.collection('users').findOne({username:u,password:p});if(user)s.json({ok:1});else s.status(401).json({ok:0})})"),
    ("javascript","app.post(\"/search\",async(r,s)=>{const results=await db.collection('products').find({$where:`this.name.includes(\"${r.body.t}\")`}).toArray();s.json(results)})","app.post(\"/search\",async(r,s)=>{if(typeof r.body.t!='string')return s.status(400).json({e:\"no\"});const results=await db.collection('products').find({name:{$regex:r.body.t,$options:'i'}}).toArray();s.json(results)})"),
    ("javascript","app.post(\"/api/users\",async(r,s)=>{const users=await db.collection('users').find(r.body.q).toArray();s.json(users)})","app.post(\"/api/users\",async(r,s)=>{const allowed=['name','email'];const q={};for(const k of Object.keys(r.body.q||{})){if(allowed.includes(k)&&typeof r.body.q[k]=='string')q[k]=r.body.q[k]}const users=await db.collection('users').find(q).toArray();s.json(users)})"),
    ("javascript","app.get(\"/user\",async(r,s)=>{const user=await db.collection('users').find({$where:`this.id==${r.query.id}`}).toArray();s.json(user)})","app.get(\"/user\",async(r,s)=>{if(!/^[a-f0-9]{24}$/.test(r.query.id))return s.status(400).json({e:\"no\"});const user=await db.collection('users').findOne({_id:ObjectId(r.query.id)});s.json(user)})"),
    # Rate Limiting
    ("python","@app.route(\"/login\")\\ndef login():\\n    if check_login(request.form[\"u\"],request.form[\"p\"]):return \"ok\"\\n    return \"no\",401","from flask_limiter import Limiter\\nlimiter=Limiter(app,key_func=lambda:request.remote_addr)\\n@app.route(\"/login\")\\n@limiter.limit(\"5/minute\")\\ndef login():\\n    if check_login(request.form[\"u\"],request.form[\"p\"]):return \"ok\"\\n    return \"no\",401"),
    ("javascript","app.post(\"/login\",(r,s)=>{const u=authenticate(r.body.u,r.body.p);if(u)s.json({t:createToken(u)});else s.status(401).json({e:\"no\"})})","const rateLimit=require('express-rate-limit');const limiter=rateLimit({windowMs:60000,max:5,message:'cok fazla'});app.post(\"/login\",limiter,(r,s)=>{const u=authenticate(r.body.u,r.body.p);if(u)s.json({t:createToken(u)});else s.status(401).json({e:\"no\"})})"),
    ("java","@PostMapping(\"/login\")ResponseEntity<?>login(@RequestBody LoginRequest r){Optional<User>u=userService.auth(r.u,r.p);if(u.isPresent())return ResponseEntity.ok(new TokenResponse(generateToken(u.get())));return ResponseEntity.status(401).build()}","@PostMapping(\"/login\")@RateLimit(limit=5,duration=60)ResponseEntity<?>login(@RequestBody LoginRequest r){Optional<User>u=userService.auth(r.u,r.p);if(u.isPresent())return ResponseEntity.ok(new TokenResponse(generateToken(u.get())));return ResponseEntity.status(401).build()}"),
    ("go","func login(w http.ResponseWriter,r*http.Request){u,err:=auth(r.FormValue(\"u\"),r.FormValue(\"p\"));if err!=nil{http.Error(w,\"no\",401);return}json.NewEncoder(w).Encode(map[string]string{\"t\":createToken(u)})}","import \"golang.org/x/time/rate\"\\nvar l=rate.NewLimiter(5,1)\\nfunc login(w http.ResponseWriter,r*http.Request){if!l.Allow(){http.Error(w,\"cok fazla\",429);return}u,err:=auth(r.FormValue(\"u\"),r.FormValue(\"p\"));if err!=nil{http.Error(w,\"no\",401);return}json.NewEncoder(w).Encode(map[string]string{\"t\":createToken(u)})}"),
    # XXE
    ("python","@app.route(\"/xml\",methods=[\"POST\"])\\ndef xml():\\n    return ET.tostring(ET.fromstring(request.data))","from lxml import etree\\np=etree.XMLParser(resolve_entities=False,no_network=True)\\n@app.route(\"/xml\",methods=[\"POST\"])\\ndef xml():\\n    return etree.tostring(etree.fromstring(request.data,p))"),
    ("javascript","app.post(\"/xml\",(r,s)=>{new xml2js.Parser().parseString(r.body.x,(e,res)=>s.json(res))})","const {XMLParser}=require('fast-xml-parser');const p=new XMLParser({processEntities:false});app.post(\"/xml\",(r,s)=>{s.json(p.parse(r.body.x))})"),
    ("java","@PostMapping(\"/xml\")String xml(@RequestBody String x)throws Exception{DocumentBuilder b=DocumentBuilderFactory.newInstance().newDocumentBuilder();return b.parse(new InputSource(new StringReader(x))).getDocumentElement().getTextContent()}","@PostMapping(\"/xml\")String xml(@RequestBody String x)throws Exception{DocumentBuilderFactory f=DocumentBuilderFactory.newInstance();f.setFeature(\"http://apache.org/xml/features/disallow-doctype-decl\",true);f.setFeature(\"http://xml.org/sax/features/external-general-entities\",false);return f.newDocumentBuilder().parse(new InputSource(new StringReader(x))).getDocumentElement().getTextContent()}"),
    # SSTI
    ("python","from flask import render_template_string\\n@app.route(\"/h\")\\ndef h():n=request.args.get(\"n\");return render_template_string(f'<h1>{n}</h1>')","from markupsafe import escape\\n@app.route(\"/h\")\\ndef h():n=request.args.get(\"n\");return render_template_string('<h1>{{n}}</h1>',n=escape(n))"),
    ("javascript","app.get(\"/g\",(r,s)=>{s.send(`<h1>${r.query.n}</h1>`)})","const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');\napp.get(\"/g\",(r,s)=>{s.send(`<h1>${esc(r.query.n)}</h1>`)})"),
    ("python","@app.route(\"/p\")\\ndef p():return render_template_string(request.args.get(\"t\"))","@app.route(\"/p\")\\ndef p():t=request.args.get(\"t\");if t not in ['<h1>{{title}}</h1>']:return 'invalid',400;return render_template_string(t,title=\"x\")"),
    # Insecure File Upload
    ("python","@app.route(\"/upload\",methods=[\"POST\"])\\ndef up():f=request.files[\"f\"];f.save(f\"/uploads/{f.filename}\");return \"ok\"","import uuid,os\\nALLOWED={\"png\",\"jpg\",\"jpeg\",\"gif\"}\\n@app.route(\"/upload\",methods=[\"POST\"])\\ndef up():f=request.files[\"f\"];ext=f.filename.rsplit(\".\",1)[1].lower()if\".\"in f.filename else\"\";if ext not in ALLOWED:return \"no\",400;fn=f\"{uuid.uuid4()}.{ext}\";f.save(f\"/uploads/{fn}\");return \"ok\""),
    ("javascript","app.post(\"/upload\",upload.single('f'),(r,s)=>{fs.renameSync(r.file.path,'/uploads/'+r.file.originalname);s.send('ok')})","app.post(\"/upload\",upload.single('f'),(r,s)=>{const ext=path.extname(r.file.originalname).toLowerCase();if(!['.png','.jpg','.jpeg'].includes(ext))return s.status(400).send('no');const n=uuid.v4()+ext;fs.renameSync(r.file.path,'/uploads/'+n);s.send('ok')})"),
    ("java","@PostMapping(\"/upload\")String up(@RequestParam MultipartFile f)throws IOException{f.transferTo(new File(\"/uploads/\"+f.getOriginalFilename()));return\"ok\"}","@PostMapping(\"/upload\")String up(@RequestParam MultipartFile f)throws IOException{String ext=StringUtils.getFilenameExtension(f.getOriginalFilename()).toLowerCase();if(!List.of(\"png\",\"jpg\",\"jpeg\").contains(ext))throw new IllegalArgumentException();f.transferTo(new File(\"/uploads/\"+UUID.randomUUID()+\".\"+ext));return\"ok\"}"),
    ("python","@app.route(\"/avatar\",methods=[\"POST\"])\\ndef av():f=request.files[\"a\"];f.save(f\"avatars/{f.filename}\");return \"ok\"","import uuid\\nALLOWED={\"png\",\"jpg\",\"jpeg\"}\\n@app.route(\"/avatar\",methods=[\"POST\"])\\ndef av():f=request.files[\"a\"];ext=f.filename.rsplit(\".\",1)[1].lower()if\".\"in f.filename else\"\";if ext not in ALLOWED or len(f.read())>5*1024*1024:return \"no\",400;f.seek(0);fn=f\"{uuid.uuid4()}.{ext}\";f.save(f\"avatars/{fn}\");return \"ok\""),
    # Mass Assignment
    ("python","@app.route(\"/api/user/update\",methods=[\"POST\"])\\ndef up():data=request.json;user=current_user;user.name=data.get(\"name\",user.name);user.email=data.get(\"email\",user.email);user.role=data.get(\"role\",user.role);db.commit();return \"ok\"","@app.route(\"/api/user/update\",methods=[\"POST\"])\\ndef up():data=request.json;user=current_user;user.name=data.get(\"name\",user.name);user.email=data.get(\"email\",user.email);db.commit();return \"ok\"  # role alanini kaldir"),
    ("javascript","app.put(\"/api/user\",(r,s)=>{db.run(\"UPDATE users SET name=?,email=?,role=? WHERE id=?\",[r.body.n,r.body.e,r.body.r,r.user.id]);s.json({ok:1})})","app.put(\"/api/user\",(r,s)=>{const{n,e}=r.body;db.run(\"UPDATE users SET name=?,email=? WHERE id=?\",[n,e,r.user.id]);s.json({ok:1})})"),
    ("java","@PutMapping(\"/api/user\")ResponseEntity<?>up(@RequestBody User u){userService.update(getUser().getId(),u);return ResponseEntity.ok().build()}","@PutMapping(\"/api/user\")ResponseEntity<?>up(@RequestBody @Valid UserUpdateDto dto){userService.update(getUser().getId(),dto);return ResponseEntity.ok().build()}"),
    # Additional: CRLF Injection
    ("python","@app.route(\"/log\")\\ndef log():msg=request.args.get(\"m\");app.logger.info(f\"User msg: {msg}\");return \"ok\"","@app.route(\"/log\")\\ndef log():msg=request.args.get(\"m\").replace(\"\\n\",\"\").replace(\"\\r\",\"\");app.logger.info(f\"User msg: {msg}\");return \"ok\""),
    ("javascript","app.get(\"/log\",(r,s)=>{console.log('Input: '+r.query.m);s.send('ok')})","app.get(\"/log\",(r,s)=>{const m=r.query.m.replace(/[\\n\\r]/g,'');console.log('Input: '+m);s.send('ok')})"),
    # Timing Attack
    ("python","def check_pass(user,pwd):\\n    stored=db.execute(\"SELECT p FROM users WHERE id=?\",(user.id,)).fetchone()[0]\\n    return stored==pwd","import hmac\\ndef check_pass(user,pwd):\\n    stored=db.execute(\"SELECT p FROM users WHERE id=?\",(user.id,)).fetchone()[0]\\n    return hmac.compare_digest(stored,pwd)"),
]
for l,bad,good in pairs_sec4:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

print(f"After sec4: {len(D)}")

pairs_sec5 = [
    # More SQL (already have 20) - add 10 more SQL across languages
    ("python","def report(start,end):\\n    q=f\"SELECT * FROM sales WHERE date>='{start}' AND date<='{end}'\"\\n    return db.execute(q).fetchall()","def report(start,end):\\n    return db.execute(\"SELECT * FROM sales WHERE date>=? AND date<=?\",(start,end)).fetchall()"),
    ("javascript","app.get(\"/sales\",(r,s)=>{db.query(`SELECT * FROM sales WHERE date>='${r.query.s}' AND date<='${r.query.e}'`,(e,rs)=>s.json(rs))})","app.get(\"/sales\",(r,s)=>{db.query(\"SELECT * FROM sales WHERE date>=? AND date<=?\",[r.query.s,r.query.e],(e,rs)=>s.json(rs))})"),
    ("java","List<Sale>getSales(String s,String e)throws SQLException{return mapSales(conn.createStatement().executeQuery(\"SELECT * FROM sales WHERE date>='\"+s+\"' AND date<='\"+e+\"'\"))}","List<Sale>getSales(String s,String e)throws SQLException{PreparedStatement ps=conn.prepareStatement(\"SELECT * FROM sales WHERE date>=? AND date<=?\");ps.setString(1,s);ps.setString(2,e);return mapSales(ps.executeQuery())}"),
    ("go","func GetSales(db *sql.DB,s,e string)([]Sale,error){rows,err:=db.Query(fmt.Sprintf(\"SELECT * FROM sales WHERE date>='%s' AND date<='%s'\",s,e));return mapSales(rows),err}","func GetSales(db *sql.DB,s,e string)([]Sale,error){rows,err:=db.Query(\"SELECT * FROM sales WHERE date>=? AND date<=?\",s,e);return mapSales(rows),err}"),
    ("web","<?php $s=$_GET[\"s\"];$e=$_GET[\"e\"];$r=mysqli_query($c,\"SELECT * FROM sales WHERE date>='$s' AND date<='$e'\");?>","<?php $stmt=$c->prepare(\"SELECT * FROM sales WHERE date>=? AND date<=?\");$stmt->bind_param(\"ss\",$s,$e);$s=$_GET[\"s\"];$e=$_GET[\"e\"];$stmt->execute();$r=$stmt->get_result();?>"),
    # More XSS (add 8)
    ("python","def render_user(u):return f'<span class=\"user\">{u[\"name\"]}</span>'","from markupsafe import escape\ndef render_user(u):return f'<span class=\"user\">{escape(u[\"name\"])}</span>'"),
    ("javascript","function showUser(u){document.getElementById('user').innerHTML='<b>'+u+'</b>'}","function showUser(u){document.getElementById('user').textContent=u}"),
    ("java","String renderUser(User u){return \"<b>\"+u.getName()+\"</b>\";}","import org.springframework.web.util.HtmlUtils;\nString renderUser(User u){return \"<b>\"+HtmlUtils.htmlEscape(u.getName())+\"</b>\";}"),
    ("go","func renderUser(w http.ResponseWriter,u User){w.Write([]byte(\"<b>\"+u.Name+\"</b>\"))}","import \"html\"\nfunc renderUser(w http.ResponseWriter,u User){w.Write([]byte(\"<b>\"+html.EscapeString(u.Name)+\"</b>\"))}"),
    ("web","<script>var n=getParam('n');document.write(n)</script>","<script>var n=getParam('n');n=n.replace(/</g,'&lt;').replace(/>/g,'&gt;');document.write(n)</script>"),
    ("javascript","$('.msg').html(userMsg)","$('.msg').text(userMsg)"),
    ("java","@GetMapping(\"/search\")@ResponseBody String search(@RequestParam String q){return \"<p>\"+q+\"</p>\";}","@GetMapping(\"/search\")@ResponseBody String search(@RequestParam String q){return \"<p>\"+HtmlUtils.htmlEscape(q)+\"</p>\";}"),
    ("python","def comment_html(c):return f'<div class=\"c\">{c[\"text\"]}</div>'","from markupsafe import escape\ndef comment_html(c):return f'<div class=\"c\">{escape(c[\"text\"])}</div>'"),
    # More CSRF (add 5)
    ("python","@app.route(\"/api/profile\",methods=[\"PUT\"])\\ndef prof():\\n    update_profile(request.json)\\n    return \"ok\"","from flask_wtf.csrf import CSRFProtect\ncsrf=CSRFProtect(app)\n@app.route(\"/api/profile\",methods=[\"PUT\"])\ndef prof():\n    update_profile(request.json)\n    return \"ok\""),
    ("javascript","app.put(\"/api/profile\",(r,s)=>{db.run(\"UPDATE profiles SET bio=? WHERE uid=?\",[r.body.bio,r.user.id]);s.json({ok:1})})","app.put(\"/api/profile\",csrf(),(r,s)=>{db.run(\"UPDATE profiles SET bio=? WHERE uid=?\",[r.body.bio,r.user.id]);s.json({ok:1})})"),
    ("java","@PutMapping(\"/api/profile\")ResponseEntity<?>profile(@RequestBody ProfileDto d){profileService.update(getUser().getId(),d);return ResponseEntity.ok().build()}","@PutMapping(\"/api/profile\")ResponseEntity<?>profile(@RequestBody ProfileDto d){profileService.update(getUser().getId(),d);return ResponseEntity.ok().build()}\n// CSRF korumasi aktif edilmeli"),
    ("go","func profile(w http.ResponseWriter,r*http.Request){uid:=r.Context().Value(\"uid\").(int);var p Profile;json.NewDecoder(r.Body).Decode(&p);db.Exec(\"UPDATE profiles SET bio=? WHERE uid=?\",p.Bio,uid);w.Write([]byte(\"ok\"))}","// CSRF middleware ile token kontrolu yap\nfunc profile(w http.ResponseWriter,r*http.Request){uid:=r.Context().Value(\"uid\").(int);var p Profile;json.NewDecoder(r.Body).Decode(&p);db.Exec(\"UPDATE profiles SET bio=? WHERE uid=?\",p.Bio,uid);w.Write([]byte(\"ok\"))}"),
    ("web","<form action=\"/profile\" method=\"POST\"><input name=\"bio\"><button>Kaydet</button></form>","<form action=\"/profile\" method=\"POST\"><input type=\"hidden\" name=\"csrf\" value=\"{{csrf}}\"><input name=\"bio\"><button>Kaydet</button></form>"),
    # More IDOR (add 5)
    ("python","@app.route(\"/api/notes/<int:nid>\")\\ndef note(nid):\\n    n=db.execute(\"SELECT * FROM notes WHERE id=?\",(nid,)).fetchone()\\n    return jsonify(dict(n))","@app.route(\"/api/notes/<int:nid>\")\\ndef note(nid):\\n    n=db.execute(\"SELECT * FROM notes WHERE id=? AND user_id=?\",(nid,current_user.id)).fetchone()\\n    if not n:return \"no\",404\\n    return jsonify(dict(n))"),
    ("javascript","app.get(\"/api/notes/:id\",(r,s)=>{db.get(\"SELECT * FROM notes WHERE id=?\",[r.params.id],(e,n)=>s.json(n))})","app.get(\"/api/notes/:id\",(r,s)=>{db.get(\"SELECT * FROM notes WHERE id=? AND user_id=?\",[r.params.id,r.user.id],(e,n)=>{if(!n)return s.status(404).json({e:\"no\"});s.json(n)})})"),
    ("java","@GetMapping(\"/api/notes/{id}\")Note get(@PathVariable Long id){return noteRepo.findById(id).orElseThrow()}","@GetMapping(\"/api/notes/{id}\")Note get(@PathVariable Long id){Note n=noteRepo.findById(id).orElseThrow();if(!n.getUserId().equals(getCurrentUser().getId()))throw new AccessDeniedException();return n}"),
    ("go","func getNote(w http.ResponseWriter,r*http.Request){id:=mux.Vars(r)[\"id\"];var n Note;db.Get(&n,\"SELECT * FROM notes WHERE id=?\",id);json.NewEncoder(w).Encode(n)}","func getNote(w http.ResponseWriter,r*http.Request){id:=mux.Vars(r)[\"id\"];uid:=r.Context().Value(\"uid\").(int);var n Note;db.Get(&n,\"SELECT * FROM notes WHERE id=? AND user_id=?\",id,uid);if n.ID==0{http.Error(w,\"no\",404);return}json.NewEncoder(w).Encode(n)}"),
    ("web","<?php $nid=$_GET[\"nid\"];$s=$db->prepare(\"SELECT * FROM notes WHERE id=?\");$s->execute([$nid]);echo json_encode($s->fetch());?>","<?php session_start();$nid=$_GET[\"nid\"];$s=$db->prepare(\"SELECT * FROM notes WHERE id=? AND user_id=?\");$s->execute([$nid,$_SESSION[\"uid\"]]);echo json_encode($s->fetch());?>"),
]
for l,bad,good in pairs_sec5:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

print(f"After sec5: {len(D)}")

pairs_ref3 = [
    # More refactoring - all remaining languages
    ("python","if len(items)==0: return True","if not items: return True"),
    ("python","def get_names():\n    conn = get_db()\n    cur = conn.cursor()\n    cur.execute(\"SELECT name FROM users\")\n    rows = cur.fetchall()\n    cur.close()\n    conn.close()\n    return [r[0] for r in rows]","def get_names():\n    with get_db() as conn:\n        cur = conn.cursor()\n        cur.execute(\"SELECT name FROM users\")\n        return [r[0] for r in cur.fetchall()]"),
    ("python","d={}\nfor k in ['a','b','c']:\n    d[k]=0","d=dict.fromkeys(['a','b','c'],0)"),
    ("python","if isinstance(x,int) or isinstance(x,float):\n    print('number')","if isinstance(x,(int,float)): print('number')"),
    ("python","def is_positive(n):\n    if n > 0:\n        return True\n    else:\n        return False","def is_positive(n): return n > 0"),
    ("python","try:\n    val = int(s)\nexcept:\n    val = 0","val = int(s) if s.isdigit() else 0"),
    ("python","for student in students:\n    print('Name:', student['name'])\n    print('Age:', student['age'])\n    print('Grade:', student['grade'])","for s in students:\n    for k,v in s.items():\n        print(f'{k.title()}: {v}')"),
    ("python","text = ''\nfor line in lines:\n    text += line + '\\n'","text = '\\n'.join(lines)"),
    ("python","c = a\nwhile c <= b:\n    print(c)\n    c += 1","for c in range(a, b+1):\n    print(c)"),
    ("python","l1=[];l2=[];l3=[]\nfor x in data:\n    l1.append(x*2)\n    l2.append(x*3)\n    l3.append(x*4)","l1,l2,l3 = [x*2 for x in data], [x*3 for x in data], [x*4 for x in data]"),
    ("python","from datetime import datetime\nprint(f'{datetime.now().strftime(\"%H:%M:%S\")}')","from datetime import datetime\nprint(f'{datetime.now():%H:%M:%S}')"),
    ("python","def get_full_name(first, last):\n    return '%s %s' % (first, last)","def get_full_name(first, last):\n    return f'{first} {last}'"),
    ("python","result = []\nfor i in range(len(items)):\n    item = items[i]\n    if item['active']:\n        result.append((i, item))","result = [(i, item) for i, item in enumerate(items) if item['active']]"),
    ("python","for key in d:\n    for subkey in d[key]:\n        print(d[key][subkey])","for key, subdict in d.items():\n    for subkey, val in subdict.items():\n        print(val)"),
    ("python","users = [{'name':'Ali'},{'name':'Veli'}]\nnames = list(map(lambda u: u['name'], users))","names = [u['name'] for u in users]"),
    ("python","total = 0\ncount = 0\nfor n in nums:\n    total += n\n    count += 1\navg = total / count","avg = sum(nums) / len(nums) if nums else 0"),
    ("python","a = 5; b = 10\nif condition:\n    a = 10; b = 5","a,b = (10,5) if condition else (5,10)"),
    ("python","def process(items, config):\n    config = config or {}\n    debug = config.get('debug', False)\n    limit = config.get('limit', 100)","def process(items, config=None):\n    config = config or {}\n    debug = config.get('debug', False)\n    limit = config.get('limit', 100)"),
    ("python","x = 1\nwhile x < 10:\n    print(x)\n    x += 1","for x in range(1, 10):\n    print(x)"),
    ("python","numbers = [-1, 2, -3, 4, -5]\npositives = []\nfor n in numbers:\n    if n > 0:\n        positives.append(n)","positives = [n for n in numbers if n > 0]"),
    # JavaScript refactoring (more)
    ("javascript","const result = [];\nfor(const x of arr){\n    if(x > 5){\n        result.push(x);\n    }\n}","const result = arr.filter(x => x > 5)"),
    ("javascript","const obj = {name:'Ali',age:25,city:'Istanbul'};\nconst name = obj.name;\nconst age = obj.age;\nconst city = obj.city;","const {name, age, city} = {name:'Ali',age:25,city:'Istanbul'}"),
    ("javascript","function greet(name){\n    if(name === undefined){\n        name = 'Guest';\n    }\n    return 'Hello ' + name;\n}","function greet(name = 'Guest'){\n    return `Hello ${name}`;\n}"),
    ("javascript","const index = arr.findIndex(x => x.id === targetId);\nif(index !== -1){\n    return arr[index];\n}","return arr.find(x => x.id === targetId)"),
    ("javascript","const filtered = [];\nfor(let i = 0; i < arr.length; i++){\n    if(arr[i].age >= 18){\n        filtered.push(arr[i].name);\n    }\n}","const filtered = arr.filter(x => x.age >= 18).map(x => x.name)"),
    ("javascript","const first = arr.slice(0, 1)[0];\nconst rest = arr.slice(1);","const [first, ...rest] = arr"),
    ("javascript","if(!arr){\n    arr = [];\n}","arr ??= []"),
    ("javascript","const fullname = person.firstName + ' ' + person.lastName;","const fullname = [person.firstName, person.lastName].filter(Boolean).join(' ')"),
    ("javascript","http.createServer((req, res) => {\n    let body = '';\n    req.on('data', chunk => body += chunk);\n    req.on('end', () => {\n        res.end('ok');\n    });\n}).listen(3000);","const express = require('express');\nconst app = express();\napp.use(express.json());\napp.post('/', (req, res) => res.send('ok'));\napp.listen(3000);"),
    ("javascript","const callback = function(){\n    console.log('done');\n};\nsetTimeout(callback, 1000);","setTimeout(() => console.log('done'), 1000);"),
    # Java refactoring (more)
    ("java","public static final double PI = 3.14159;","import static java.lang.Math.PI;"),
    ("java","String result = \"\"; for(String s : list){ result += s + \",\"; }","String result = String.join(\",\", list);"),
    ("java","public boolean check(int x){\n    if(x > 0 && x < 100){\n        return true;\n    } else {\n        return false;\n    }\n}","public boolean check(int x){ return x > 0 && x < 100; }"),
    ("java","List<String> names = new ArrayList<>();\nfor(User u : users){\n    names.add(u.getName());\n}","List<String> names = users.stream().map(User::getName).toList();"),
    ("java","if(collection.size() > 0){\n    return collection.get(0);\n}\nreturn null;","return collection.isEmpty() ? null : collection.get(0);"),
    ("java","try{\n    Connection c = dataSource.getConnection();\n    // use c\n    c.close();\n} catch(SQLException e){\n    log.error(e);\n}","try(Connection c = dataSource.getConnection()){\n    // use c\n} catch(SQLException e){\n    log.error(e);\n}"),
    ("java","public boolean isValidEmail(String email){\n    Pattern p = Pattern.compile(\"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\\\.[A-Z]{2,6}$\", Pattern.CASE_INSENSITIVE);\n    Matcher m = p.matcher(email);\n    return m.find();\n}","public boolean isValidEmail(String email){\n    return email != null && email.matches(\"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\\\.[A-Z]{2,6}$\");\n}"),
    ("java","if(str == null || str.equals(\"\")){\n    return true;\n}","if(str == null || str.isEmpty()){\n    return true;\n}"),
    ("java","int count = 0;\nfor(Item i : items){\n    if(i.isActive()){\n        count++;\n    }\n}","long count = items.stream().filter(Item::isActive).count();"),
    ("java","Map<String, Object> params = new HashMap<>();\nparams.put(\"name\", name);\nparams.put(\"age\", age);","var params = Map.of(\"name\", name, \"age\", age);"),
    # Go refactoring (more)
    ("go","x := 5\nif x > 10 {\n    y := 20\n} else {\n    y := 0\n}","y := 0\nif x > 10 { y = 20 }"),
    ("go","for i, val := range items {\n    items[i] = val * 2\n}","for i := range items {\n    items[i] *= 2\n}"),
    ("go","s := make([]int, 0, 10)\nfor i := 0; i < 10; i++ {\n    s = append(s, i)\n}","s := make([]int, 10)\nfor i := range s {\n    s[i] = i\n}"),
    ("go","if x == 0 || x == 1 {\n    return true\n}","switch x { case 0,1: return true }"),
    ("go","var result int\nfor _, n := range numbers {\n    if n > 0 {\n        result += n\n    }\n}","result := 0\nfor _, n := range numbers {\n    if n > 0 { result += n }\n}"),
    ("go","bytes, err := ioutil.ReadAll(r.Body)\nif err != nil {\n    http.Error(w, err.Error(), 500)\n    return\n}","bytes, err := io.ReadAll(r.Body)\nif err != nil { http.Error(w, err.Error(), 500); return }"),
    ("go","x := 10\nif x == 10 {\n    fmt.Println(\"true\")\n} else {\n    fmt.Println(\"false\")\n}","if x == 10 { fmt.Println(\"true\") } else { fmt.Println(\"false\") }"),
    ("go","type Point struct {\n    X int\n    Y int\n}\nfunc (p Point) Dist() float64 {\n    return math.Sqrt(float64(p.X*p.X + p.Y*p.Y))\n}","type Point struct{ X,Y int }\nfunc (p Point) Dist() float64 { return math.Hypot(float64(p.X), float64(p.Y)) }"),
    ("go","name := \"\"\nif n := r.FormValue(\"name\"); n != \"\" {\n    name = n\n} else {\n    name = \"Guest\"\n}","name := r.FormValue(\"name\")\nif name == \"\" { name = \"Guest\" }"),
    ("go","var m = map[string]int{\"a\": 1}\nval, ok := m[\"b\"]\nif ok {\n    fmt.Println(val)\n} else {\n    fmt.Println(\"not found\")\n}","if val, ok := m[\"b\"]; ok { fmt.Println(val) } else { fmt.Println(\"not found\") }"),
    # TypeScript refactoring (more)
    ("typescript","enum Direction { Up = 0, Down = 1, Left = 2, Right = 3 }","const enum Direction { Up, Down, Left, Right }"),
    ("typescript","const items: Array<{id: number, name: string}> = []","const items: {id: number, name: string}[] = []"),
    ("typescript","function map<T, U>(arr: T[], fn: (x: T) => U): U[] {\n    return arr.map(fn)\n}","// Already in standard library"),
    ("typescript","class Person {\n    private _name: string;\n    constructor(name: string) { this._name = name; }\n    public getName(): string { return this._name; }\n    public setName(v: string) { this._name = v; }\n}","class Person {\n    constructor(public name: string) {}\n}"),
    ("typescript","const val = obj !== null && obj !== undefined ? obj : 'default'","const val = obj ?? 'default'"),
    ("typescript","type APIResponse = {\n    status: number;\n    data: any;\n    error: string | null;\n}","interface APIResponse<T> {\n    status: number;\n    data: T;\n    error: string | null;\n}"),
    ("typescript","function process(arr: (string | number)[]) {\n    for(let i = 0; i < arr.length; i++) {\n        console.log(arr[i]);\n    }\n}","function process(arr: (string | number)[]) {\n    arr.forEach(x => console.log(x));\n}"),
    ("typescript","const result = await fetch('/api').then(r => r.json());","const response = await fetch('/api');\nconst result = await response.json();"),
    ("typescript","let id: string | null = localStorage.getItem('id');\nif(id === null) id = 'default';","const id = localStorage.getItem('id') ?? 'default';"),
    ("typescript","const filtered = arr.filter(x => x != null).map(x => x!.toString())","const filtered = arr.filter((x): x is NonNullable<typeof x> => x != null).map(x => x.toString())"),
    ("typescript","function sleep(ms: number): Promise<void> {\n    return new Promise(r => setTimeout(r, ms));\n}","const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));"),
    ("typescript","function getLength(x: string | any[]): number {\n    if(typeof x === 'string') return x.length;\n    return x.length;\n}","function getLength(x: {length: number}): number { return x.length; }"),
    ("typescript","import { Component } from 'react';\n\nclass MyComp extends Component {","import { FC } from 'react';\n\nconst MyComp: FC = () => {"),
    ("typescript","const result: {[key: string]: number} = {}","const result: Record<string, number> = {}"),
    ("typescript","function parseNum(s: string | null): number {\n    if(s !== null) return parseInt(s, 10);\n    return 0;\n}","const parseNum = (s: string | null): number => parseInt(s ?? '0', 10);"),
]
for l,bad,good in pairs_ref3:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)

print(f"After ref3: {len(D)}")

# Final write
with open(O,"w",encoding="utf-8") as f:
    json.dump(D,f,ensure_ascii=False,indent=2)
print(f"Written to {O}")

# ===== Final batch to reach 600 =====
pairs_final = [
    # Security: Python (+36)
    ("python","@app.route(\"/transfer\")\\ndef t():\\n    a=request.form[\"a\"]\\n    t=request.form[\"t\"]\\n    transfer_money(current_user,t,a)\\n    return \"OK\"","@app.route(\"/transfer\")\\n@csrf.exempt\\ndef t():\\n    a=request.form[\"a\"]\\n    t=request.form[\"t\"]\\n    transfer_money(current_user,t,a)\\n    return \"OK\"  # CSRF token kullanilmali"),
    ("python","@app.route(\"/del\",methods=[\"POST\"])\\ndef d():\\n    if request.form[\"confirm\"]==\"yes\":\\n        db.execute(\"DELETE FROM users WHERE id=?\",(session[\"uid\"],))\\n        return redirect(\"/\")\\n    return \"no\"","@app.route(\"/del\",methods=[\"POST\"])\\ndef d():\\n    if request.form.get(\"csrf\")!=session.pop(\"csrf\",None):abort(403)\\n    if request.form[\"confirm\"]==\"yes\":\\n        db.execute(\"DELETE FROM users WHERE id=?\",(session[\"uid\"],))\\n        return redirect(\"/\")"),
    ("python","@app.route(\"/create_user\",methods=[\"POST\"])\\ndef cu():\\n    data=request.json\\n    db.execute(\"INSERT INTO users(name,email,role) VALUES(?,?,?)\",(data[\"n\"],data[\"e\"],data.get(\"r\",\"user\")))\\n    db.commit()\\n    return \"ok\"","@app.route(\"/create_user\",methods=[\"POST\"])\\ndef cu():\\n    data=request.json\\n    db.execute(\"INSERT INTO users(name,email) VALUES(?,?)\",(data[\"n\"],data[\"e\"]))\\n    db.commit()\\n    return \"ok\"  # role mass assignment engellendi"),
    ("python","def generate_code():\n    import random\n    return ''.join(random.choice('0123456789') for _ in range(6))","import secrets, string\ndef generate_code():\n    return ''.join(secrets.choice(string.digits) for _ in range(6))"),
    ("python","@app.route('/api/config')\ndef config():\n    return jsonify({'db': os.environ.get('DATABASE_URL'), 'secret': os.environ.get('SECRET_KEY')})","@app.route('/api/config')\ndef config():\n    return jsonify({'status': 'ok'})"),
    ("python","import hashlib, os\nsalt = 'fixed_salt'\ndef hash_pw(p): return hashlib.sha256((salt + p).encode()).hexdigest()","import bcrypt\ndef hash_pw(p): return bcrypt.hashpw(p.encode(), bcrypt.gensalt())"),
    ("python","from Crypto.Cipher import AES\ndef encrypt(data):\n    cipher = AES.new(b'1234567890123456', AES.MODE_ECB)\n    return cipher.encrypt(data)","from Crypto.Cipher import AES\nimport os\ndef encrypt(data):\n    iv = os.urandom(16)\n    cipher = AES.new(b'1234567890123456', AES.MODE_CBC, iv=iv)\n    return iv + cipher.encrypt(data)"),
    ("python","@app.route(\"/api/export\")\ndef export():\n    data = db.execute(\"SELECT * FROM users\").fetchall()\n    return Response(json.dumps([dict(r) for r in data]), mimetype='application/json')","@app.route(\"/api/export\")\n@login_required\ndef export():\n    if not current_user.is_admin: return 'no', 403\n    data = db.execute(\"SELECT id, name, email FROM users\").fetchall()\n    return jsonify([dict(r) for r in data])"),
    ("python","@app.route(\"/file\")\ndef file():\n    p = request.args.get(\"p\")\n    return send_file(p)","@app.route(\"/file\")\ndef file():\n    p = request.args.get(\"p\")\n    base = os.path.abspath(\".\")\n    full = os.path.normpath(os.path.join(base, p))\n    if not full.startswith(base): return 'no', 403\n    return send_file(full)"),
]
for l,bad,good in pairs_final:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

pairs_final2 = [
    # Security: JavaScript (+6), Java (+11), Go (+5), Web (+16)
    ("javascript","app.post('/signup',(r,s)=>{const{name,email,role}=r.body;db.run('INSERT INTO users(name,email,role) VALUES(?,?,?)',[name,email,role||'user']);s.json({ok:1})})","app.post('/signup',(r,s)=>{const{name,email}=r.body;db.run('INSERT INTO users(name,email) VALUES(?,?)',[name,email]);s.json({ok:1})})"),
    ("javascript","const token = req.cookies.token;\nif(token){\n    const user = parseToken(token);\n    req.user = user;\n}","const authHeader = req.headers.authorization;\nif(authHeader && authHeader.startsWith('Bearer ')){\n    const token = authHeader.slice(7);\n    try{\n        req.user = jwt.verify(token, process.env.JWT_SECRET);\n    }catch{ return res.status(401).send('no'); }\n}"),
    ("javascript","app.get('/debug',(r,s)=>{s.json({env:process.env,config:app.get('config')})})","app.get('/health',(r,s)=>{s.json({status:'ok'})})"),
    ("javascript","const exec = require('child_process').exec;\napp.post('/exec',(r,s)=>{exec(r.body.cmd,(e,o)=>s.send(o))})","const {execFile} = require('child_process');\napp.post('/exec',(r,s)=>{s.status(403).send('disabled')})"),
    ("javascript","function validate(user){\n    return eval('user.admin === true');\n}","function validate(user){\n    return user.admin === true;\n}"),
    ("javascript","app.get('/proxy',(r,s)=>{const target = r.query.url;s.redirect(target)})","app.get('/proxy',(r,s)=>{const target = r.query.url;const allowed = ['https://example.com'];if(!allowed.includes(target))return s.status(400).send('no');s.redirect(target)})"),
    # Java security
    ("java","@GetMapping(\"/api/search\")List<Item>search(@RequestParam String q)throws SQLException{Statement s=conn.createStatement();return mapItems(s.executeQuery(\"SELECT * FROM items WHERE name LIKE '%\"+q+\"%'\"))}","@GetMapping(\"/api/search\")List<Item>search(@RequestParam String q)throws SQLException{PreparedStatement ps=conn.prepareStatement(\"SELECT * FROM items WHERE name LIKE ?\");ps.setString(1,\"%\"+q+\"%\");return mapItems(ps.executeQuery())}"),
    ("java","@GetMapping(\"/api/users/{id}\")User getUser(@PathVariable String id){return userRepo.findById(id).orElse(null)}","@GetMapping(\"/api/users/{id}\")User getUser(@PathVariable String id){User u=userRepo.findById(id).orElse(null);if(u==null||!u.getTenantId().equals(getCurrentUser().getTenantId()))throw new AccessDeniedException();return u}"),
    ("java","@PostMapping(\"/api/save\")ResponseEntity<?>save(@RequestBody User u){userRepo.save(u);return ResponseEntity.ok().build()}","@PostMapping(\"/api/save\")ResponseEntity<?>save(@RequestBody @Valid UserCreateDto dto){User u=new User();u.setName(dto.getName());u.setEmail(dto.getEmail());userRepo.save(u);return ResponseEntity.ok().build()}"),
    ("java","public boolean checkPassword(String raw,String stored){return raw.equals(stored);}","public boolean checkPassword(String raw,String stored){return BCrypt.checkpw(raw,stored);}"),
    ("java","@GetMapping(\"/admin/config\")Properties config(){return System.getProperties();}","@GetMapping(\"/admin/config\")@PreAuthorize(\"hasRole('ADMIN')\")Properties config(){SecurityManager sm=System.getSecurityManager();if(sm!=null)sm.checkPermission(new RuntimePermission(\"getProperties\"));return System.getProperties();}"),
    ("java","public void runScript(String script)throws IOException{Runtime.getRuntime().exec(script);}","public void runScript(String script)throws IOException{if(!script.matches(\"^[a-zA-Z0-9_.-/]+\"))throw new IllegalArgumentException();Runtime.getRuntime().exec(new String[]{\"/bin/sh\",\"-c\",script});}"),
    ("java","@PostMapping(\"/upload\")String upload(@RequestParam(\"file\")MultipartFile f)throws IOException{f.transferTo(new File(\"/tmp/\"+f.getOriginalFilename()));return\"ok\"}","@PostMapping(\"/upload\")String upload(@RequestParam(\"file\")MultipartFile f)throws IOException{String[]allowed={\"jpg\",\"png\",\"pdf\"};String ext=f.getOriginalFilename().substring(f.getOriginalFilename().lastIndexOf('.')+1).toLowerCase();if(!List.of(allowed).contains(ext))throw new IllegalArgumentException();String name=UUID.randomUUID()+\".\"+ext;f.transferTo(new File(\"/uploads/\"+name));return\"ok\"}"),
    ("java","@GetMapping(\"/external/fetch\")String fetch(@RequestParam String u)throws IOException{return new String(new URL(u).openStream().readAllBytes());}","@GetMapping(\"/external/fetch\")String fetch(@RequestParam String u)throws IOException{URI uri=new URI(u);InetAddress a=InetAddress.getByName(uri.getHost());if(a.isLoopbackAddress()||a.isSiteLocalAddress())throw new SecurityException();HttpURLConnection c=(HttpURLConnection)uri.toURL().openConnection();c.setConnectTimeout(5000);try(var r=new BufferedReader(new InputStreamReader(c.getInputStream()))){return r.lines().collect(Collectors.joining())}}"),
    ("java","@GetMapping(\"/api/orders/{id}\")Order order(@PathVariable Long id){return orderRepo.findById(id).orElseThrow();}","@GetMapping(\"/api/orders/{id}\")Order order(@PathVariable Long id){Order o=orderRepo.findById(id).orElseThrow();if(!o.getUserId().equals(getCurrentUser().getId()))throw new AccessDeniedException();return o;}"),
    ("java","@PostMapping(\"/login\")String login(@RequestParam String u,@RequestParam String p,HttpSession s){if(\"admin\".equals(u)&&\"admin\".equals(p)){s.setAttribute(\"user\",u);return\"ok\"}return\"no\"}","@PostMapping(\"/login\")String login(@RequestParam String u,@RequestParam String p,HttpServletRequest r){User user=userService.auth(u,p);if(user!=null){HttpSession s=r.getSession(true);s.setAttribute(\"userId\",user.getId());return\"ok\"}return\"no\"}"),
    # Go security (+5)
    ("go","func search(w http.ResponseWriter,r*http.Request){q:=r.URL.Query().Get(\"q\");rows,_:=db.Query(fmt.Sprintf(\"SELECT * FROM items WHERE name LIKE '%%%s%%'\",q));json.NewEncoder(w).Encode(mapItems(rows))}","func search(w http.ResponseWriter,r*http.Request){q:=r.URL.Query().Get(\"q\");rows,err:=db.Query(\"SELECT * FROM items WHERE name LIKE ?\",\"%\"+q+\"%\");if err!=nil{http.Error(w,\"err\",500);return}json.NewEncoder(w).Encode(mapItems(rows))}"),
    ("go","func up(w http.ResponseWriter,r*http.Request){r.ParseMultipartForm(32<<20);f,_,_:=r.FormFile(\"f\");defer f.Close();b,_:=ioutil.ReadAll(f);ioutil.WriteFile(\"/uploads/\"+f.Filename,b,0644);w.Write([]byte(\"ok\"))}","func up(w http.ResponseWriter,r*http.Request){r.ParseMultipartForm(32<<20);f,h,_:=r.FormFile(\"f\");defer f.Close();allowed:=map[string]bool{\".jpg\":true,\".png\":true};ext:=filepath.Ext(h.Filename);if!allowed[ext]{http.Error(w,\"no\",400);return}b,_:=ioutil.ReadAll(f);n:=uuid.New().String()+ext;ioutil.WriteFile(\"/uploads/\"+n,b,0644);w.Write([]byte(\"ok\"))}"),
    ("go","type User struct{Id int;Name string;Email string;Role string}\nfunc update(w http.ResponseWriter,r*http.Request){var u User;json.NewDecoder(r.Body).Decode(&u);db.Exec(\"UPDATE users SET name=?,email=?,role=? WHERE id=?\",u.Name,u.Email,u.Role,u.Id)}","func update(w http.ResponseWriter,r*http.Request){var u struct{Name string;Email string};json.NewDecoder(r.Body).Decode(&u);db.Exec(\"UPDATE users SET name=?,email=? WHERE id=?\",u.Name,u.Email,r.Context().Value(\"uid\"))}"),
    ("go","func health(w http.ResponseWriter,r*http.Request){host,_:=os.Hostname();w.Write([]byte(fmt.Sprintf(\"Host:%s,User:%s\",host,r.Header.Get(\"X-User\"))))}","func health(w http.ResponseWriter,r*http.Request){w.Write([]byte(\"ok\"))}"),
    ("go","func download(w http.ResponseWriter,r*http.Request){f:=r.URL.Query().Get(\"f\");http.ServeFile(w,r,\"/data/\"+f)}","func download(w http.ResponseWriter,r*http.Request){f:=r.URL.Query().Get(\"f\");if strings.Contains(f,\"..\")||strings.Contains(f,\"/\"){http.Error(w,\"no\",400);return}http.ServeFile(w,r,\"/data/\"+f)}"),
    # Web security (+16)
    ("web","<?php $id=$_GET[\"id\"];$r=mysqli_query($c,\"SELECT * FROM users WHERE id=$id\");?>","<?php $stmt=$c->prepare(\"SELECT * FROM users WHERE id=?\");$stmt->bind_param(\"i\",$id);$id=$_GET[\"id\"];$stmt->execute();$r=$stmt->get_result();?>"),
    ("web","<?php echo \"<h1>Merhaba \".$_GET[\"name\"].\"</h1>\";?>","<?php echo \"<h1>Merhaba \".htmlspecialchars($_GET[\"name\"]).\"</h1>\";?>"),
    ("web","<?php $r=file_get_contents($_GET[\"url\"]);echo $r;?>","<?php $u=$_GET[\"url\"];$p=parse_url($u);if(in_array($p[\"host\"],[\"127.0.0.1\",\"localhost\"])){die();}$r=file_get_contents($u,false,stream_context_create([\"http\"=>[\"timeout\"=>5]]));echo $r;?>"),
    ("web","<?php session_start();$_SESSION[\"user\"]=$_POST[\"user\"];?>","<?php session_start();session_regenerate_id(true);$_SESSION[\"user\"]=$_POST[\"user\"];?>"),
    ("web","<?php setcookie(\"auth\",$token);?>","<?php setcookie(\"auth\",$token,time()+3600,\"/\",\"\",true,true);?>"),
    ("web","<?php $f=$_GET[\"file\"];include(\"pages/\".$f);?>","<?php $f=$_GET[\"file\"];$f=str_replace(\"..\",\"\",$f);$f=basename($f);include(\"pages/\".$f);?>"),
    ("web","<?php $pass=md5($_POST[\"p\"]);$db->query(\"INSERT INTO users(password)VALUES('$pass')\");?>","<?php $pass=password_hash($_POST[\"p\"],PASSWORD_BCRYPT);$stmt=$db->prepare(\"INSERT INTO users(password)VALUES(?)\");$stmt->execute([$pass]);?>"),
    ("web","<?php $cmd=$_GET[\"cmd\"];system($cmd);?>","<?php $cmd=$_GET[\"cmd\"];if(!in_array($cmd,[\"ls\",\"pwd\"]))die();system(escapeshellcmd($cmd));?>"),
    ("web","<?php eval(\$x = $_POST['code']);?>","<?php // eval kullanma; alternative logic here?>"),
    ("web","<?php $data=unserialize($_COOKIE[\"s\"]);?>","<?php $data=json_decode($_COOKIE[\"s\"],true);?>"),
    ("web","<?php $file=$_GET[\"f\"];header(\"Content-Type: application/pdf\");readfile(\"/docs/\".$file);?>","<?php $file=$_GET[\"f\"];$file=basename($file);$path=realpath(\"/docs/\".$file);if(!$path||strpos($path,realpath(\"/docs\"))!==0){die();}header(\"Content-Type: application/pdf\");readfile($path);?>"),
    ("web","<?php $db=new PDO(\"mysql:host=localhost;dbname=test\",\"root\",\"\");?>","<?php $db=new PDO(\"mysql:host=localhost;dbname=test;charset=utf8mb4\",getenv(\"DB_USER\"),getenv(\"DB_PASS\"),[PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION,PDO::ATTR_EMULATE_PREPARES=>false]);?>"),
    ("web","<script>\n  var data = eval(localStorage.getItem('userData'));\n</script>","<script>\n  var data = JSON.parse(localStorage.getItem('userData'));\n</script>"),
    ("web","<form action=\"/delete\" method=\"POST\">\n  <input name=\"id\" type=\"hidden\" value=\"1\">\n  <button>Sil</button>\n</form>","<form action=\"/delete\" method=\"POST\">\n  <input type=\"hidden\" name=\"csrf\" value=\"<?=$csrf?>\">\n  <input name=\"id\" type=\"hidden\" value=\"1\">\n  <button>Sil</button>\n</form>"),
    ("web","<?php\n$role = $_POST['role'];\n$query = $db->prepare(\"INSERT INTO users(role) VALUES(?)\");\n$query->execute([$role]);\n?>","<?php\n$role = 'user'; // sabit rol, kullanicidan alinmaz\n$query = $db->prepare(\"INSERT INTO users(role) VALUES(?)\");\n$query->execute([$role]);\n?>"),
    ("web","<?php\nheader('Location: ' . $_SERVER['HTTP_REFERER']);\n?>","<?php\n$ref = $_SERVER['HTTP_REFERER'] ?? '/';\n$parsed = parse_url($ref);\n$allowed_hosts = ['example.com'];\nif(!in_array($parsed['host'] ?? '', $allowed_hosts)) $ref = '/';\nheader('Location: ' . $ref);\n?>"),
]
for l,bad,good in pairs_final:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)
for l,bad,good in pairs_final2:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)

print(f"After final security: {len(D)}")

pairs_ref4 = [
    # More refactoring pairs (Python, JS, Java, Go, TS)
    ("python","def send_notification(user, title, msg, channel, priority):\n    if channel == \"email\":\n        send_email(user.email, title, msg)\n    elif channel == \"sms\":\n        send_sms(user.phone, msg)\n    elif channel == \"push\":\n        send_push(user.device_token, title, msg)","class Notification:\n    def __init__(self, user): self.user = user\n    def send_email(self, title, msg): send_email(self.user.email, title, msg)\n    def send_sms(self, msg): send_sms(self.user.phone, msg)\n    def send_push(self, title, msg): send_push(self.user.device_token, title, msg)"),
    ("python","def calculate_total(items):\n    t = 0\n    for i in items:\n        t += i.price * i.quantity\n        if i.is_taxable:\n            t += i.price * i.quantity * 0.08\n    return t","def calculate_total(items):\n    return sum(i.price * i.quantity * (1.08 if i.is_taxable else 1) for i in items)"),
    ("python","def get_data():\n    r = requests.get(\"https://api.example.com/data\")\n    return r.json()\n\ndef filter_active(data):\n    return [d for d in data if d[\"active\"]]\n\ndef transform(data):\n    return [{\"id\": d[\"id\"], \"name\": d[\"name\"].upper()} for d in data]","def get_active_data():\n    data = requests.get(\"https://api.example.com/data\").json()\n    return [{\"id\": d[\"id\"], \"name\": d[\"name\"].upper()} for d in data if d[\"active\"]]"),
    ("python","for i in range(len(customers)):\n    c = customers[i]\n    for j in range(len(orders)):\n        o = orders[j]\n        if c[\"id\"] == o[\"customer_id\"]:\n            print(c[\"name\"], o[\"total\"])","for c in customers:\n    for o in orders:\n        if c[\"id\"] == o[\"customer_id\"]:\n            print(c[\"name\"], o[\"total\"])"),
    ("python","user = db.execute(\"SELECT * FROM users WHERE id=?\", (uid,)).fetchone()\nif user:\n    display_name = user[\"first\"] + \" \" + user[\"last\"]\nelse:\n    display_name = \"Misafir\"","user = db.execute(\"SELECT * FROM users WHERE id=?\", (uid,)).fetchone()\ndisplay_name = f\"{user['first']} {user['last']}\" if user else \"Misafir\""),
    ("python","def handle_request(request):\n    if request.type == \"create\":\n        return create_item(request.data)\n    elif request.type == \"update\":\n        return update_item(request.id, request.data)\n    elif request.type == \"delete\":\n        return delete_item(request.id)\n    elif request.type == \"read\":\n        return get_item(request.id)","HANDLERS = {\n    \"create\": lambda r: create_item(r.data),\n    \"update\": lambda r: update_item(r.id, r.data),\n    \"delete\": lambda r: delete_item(r.id),\n    \"read\": lambda r: get_item(r.id),\n}\ndef handle_request(request):\n    handler = HANDLERS.get(request.type)\n    if handler: return handler(request)\n    raise ValueError(f\"Unknown type: {request.type}\")"),
    ("python","def get_largest(numbers):\n    max_num = numbers[0]\n    for n in numbers:\n        if n > max_num:\n            max_num = n\n    return max_num","def get_largest(numbers):\n    return max(numbers) if numbers else None"),
    ("python","def create_user(name, email, age=None, phone=None, address=None, city=None):\n    user = {\"name\": name, \"email\": email}\n    if age: user[\"age\"] = age\n    if phone: user[\"phone\"] = phone\n    if address: user[\"address\"] = address\n    if city: user[\"city\"] = city\n    return user","def create_user(name, email, **kwargs):\n    return {\"name\": name, \"email\": email, **{k: v for k, v in kwargs.items() if v}})"),
    ("python","def file_extension(filename):\n    parts = filename.split(\".\")\n    if len(parts) > 1:\n        return parts[-1]\n    return \"\"","def file_extension(filename):\n    return filename.rsplit(\".\", 1)[-1] if \".\" in filename else \"\""),
    ("python","def get_active_items(data):\n    active = []\n    for item in data:\n        if item.status == \"active\":\n            active.append(item)\n    return sorted(active, key=lambda x: x.created_at)","def get_active_items(data):\n    return sorted((item for item in data if item.status == \"active\"), key=lambda x: x.created_at)"),
    ("python","if a and b and c and d and e:\n    process()","if all([a, b, c, d, e]):\n    process()"),
    ("python","for x in iterable:\n    if condition(x):\n        first = x\n        break\nelse:\n    first = None","first = next((x for x in iterable if condition(x)), None)"),
    ("python","result = []\nfor x in list1:\n    for y in list2:\n        result.append((x, y))","from itertools import product\nresult = list(product(list1, list2))"),
    ("python","def save_user(user):\n    if user.id is None:\n        db.execute(\"INSERT INTO users(name) VALUES(?)\", (user.name,))\n    else:\n        db.execute(\"UPDATE users SET name=? WHERE id=?\", (user.name, user.id))","def save_user(user):\n    if user.id is None:\n        db.execute(\"INSERT INTO users(name) VALUES(?)\", (user.name,))\n    else:\n        db.execute(\"UPDATE users SET name=? WHERE id=?\", (user.name, user.id))  # upsert pattern"),
]
for l,bad,good in pairs_ref4:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)

print(f"After ref4: {len(D)}")

# Final write to capture all data
with open(O,"w",encoding="utf-8") as f:
    json.dump(D,f,ensure_ascii=False,indent=2)
print(f"FINAL written {len(D)} pairs to {O}")

pairs_final3 = [
    # Security Python (+18)
    ("python","from Crypto.Cipher import AES, DES\ndef encrypt(plain,key): return DES.new(key,DES.MODE_ECB).encrypt(plain)","from Crypto.Cipher import AES\nimport os\ndef encrypt(plain,key):\n    iv=os.urandom(16)\n    return iv+AES.new(key,AES.MODE_CBC,iv=iv).encrypt(plain)"),
    ("python","import random\ndef gen_otp(): return str(random.randint(100000,999999))","import secrets\ndef gen_otp(): return str(secrets.randbelow(900000)+100000)"),
    ("python","@app.route(\"/api/user/search\")\ndef search():\n    q=request.args.get(\"q\")\n    return jsonify(db.execute(f\"SELECT * FROM users WHERE name LIKE '%{q}%'\").fetchall())","@app.route(\"/api/user/search\")\ndef search():\n    q=request.args.get(\"q\")\n    return jsonify(db.execute(\"SELECT * FROM users WHERE name LIKE ?\",('%'+q+'%',)).fetchall())"),
    ("python","import hashlib, os\ndef encrypt_pwd(p,salt): return hashlib.pbkdf2_hmac('sha1',p.encode(),salt,1000).hex()","import hashlib, os\ndef encrypt_pwd(p,salt): return hashlib.pbkdf2_hmac('sha256',p.encode(),salt,600000).hex()"),
    ("python","@app.route(\"/admin/logs\")\ndef logs():\n    f=request.args.get(\"f\")\n    return open(f\"/var/log/{f}\").read()","import os\n@app.route(\"/admin/logs\")\ndef logs():\n    f=request.args.get(\"f\")\n    if '..' in f or '/' in f: return 'no',400\n    return open(f\"/var/log/{f}\").read()"),
    ("python","class Config:\n    SECRET_KEY='hardcoded-secret-key'\n    DB_PASSWORD='password123'","import os\nclass Config:\n    SECRET_KEY=os.environ.get('SECRET_KEY','fallback-dev-key')\n    DB_PASSWORD=os.environ.get('DB_PASSWORD')"),
    ("python","@app.route(\"/api/items\",methods=[\"POST\"])\ndef create():\n    item=Item(request.json)\n    db.add(item)\n    db.commit()\n    return jsonify(item.to_dict())","@app.route(\"/api/items\",methods=[\"POST\"])\n@login_required\ndef create():\n    item=Item(request.json)\n    item.user_id=current_user.id\n    db.add(item)\n    db.commit()\n    return jsonify(item.to_dict())"),
    ("python","def verify(jwt_token,secret): return jwt.decode(jwt_token,secret,algorithms=['HS256','none'])","def verify(jwt_token,secret): return jwt.decode(jwt_token,secret,algorithms=['HS256'])"),
    ("python","@app.route(\"/api/token\")\ndef token():\n    return jwt.encode({'user':request.args.get('u')},'secret',algorithm='HS256')","@app.route(\"/api/token\")\ndef token():\n    if not current_user.is_authenticated: return 'no',401\n    return jwt.encode({'user':current_user.id,'exp':datetime.utcnow()+timedelta(hours=1)},current_user.secret,algorithm='HS256')"),
    ("python","import xml.etree.ElementTree as ET\n@app.route(\"/api/xml\")\ndef xml():\n    return ET.tostring(ET.fromstring(request.data))","from lxml import etree\np=etree.XMLParser(resolve_entities=False,no_network=True)\n@app.route(\"/api/xml\")\ndef xml():\n    return etree.tostring(etree.fromstring(request.data,p))"),
    ("python","def get_session():\n    data=request.cookies.get('session')\n    if data: return pickle.loads(base64.b64decode(data))","import json\ndef get_session():\n    data=request.cookies.get('session')\n    if data: return json.loads(base64.b64decode(data).decode())"),
    ("python","@app.route(\"/api/search\")\n@login_required\ndef search():\n    q=request.args.get(\"q\")\n    return jsonify(db.execute(f\"SELECT * FROM items WHERE name LIKE '%{q}%' AND user_id={current_user.id}\").fetchall())","@app.route(\"/api/search\")\n@login_required\ndef search():\n    q=request.args.get(\"q\")\n    return jsonify(db.execute(\"SELECT * FROM items WHERE name LIKE ? AND user_id=?\",('%'+q+'%',current_user.id)).fetchall())"),
    ("python","@app.route(\"/login\",methods=[\"POST\"])\ndef login():\n    u=db.execute(\"SELECT * FROM users WHERE username=?\",(request.form['u'],)).fetchone()\n    if u and request.form['p']==u['password']:\n        session['uid']=u['id']\n        return 'ok'\n    return 'no'","@app.route(\"/login\",methods=[\"POST\"])\ndef login():\n    u=db.execute(\"SELECT * FROM users WHERE username=?\",(request.form['u'],)).fetchone()\n    if u and bcrypt.checkpw(request.form['p'].encode(),u['password'].encode()):\n        session.clear()\n        session['uid']=u['id']\n        return 'ok'\n    return 'no',401"),
    ("python","@app.route(\"/logout\")\ndef logout():\n    session.pop('uid',None)\n    return redirect('/')","@app.route(\"/logout\")\ndef logout():\n    session.clear()\n    return redirect('/')"),
    ("python","@app.route(\"/proxy_image\")\ndef proxy():\n    url=request.args.get('url')\n    return requests.get(url).content","@app.route(\"/proxy_image\")\ndef proxy():\n    url=request.args.get('url')\n    parsed=urlparse(url)\n    if parsed.hostname not in ['cdn.example.com']: return 'no',403\n    return requests.get(url,timeout=5).content"),
    ("python","@app.route(\"/api/notes\")\ndef notes():\n    return jsonify(db.execute(\"SELECT * FROM notes\").fetchall())","@app.route(\"/api/notes\")\n@login_required\ndef notes():\n    return jsonify(db.execute(\"SELECT * FROM notes WHERE user_id=?\",(current_user.id,)).fetchall())"),
    ("python","from Crypto.Cipher import AES\nkey=os.urandom(16)\ndef encrypt(data):\n    c=AES.new(key,AES.MODE_CTR)\n    return c.encrypt(data)","from Crypto.Cipher import AES\nimport os\nkey=os.urandom(32)\ndef encrypt(data):\n    nonce=os.urandom(8)\n    c=AES.new(key,AES.MODE_CTR,nonce=nonce)\n    return nonce+c.encrypt(data)"),
    ("python","@app.route(\"/api/transfer\")\ndef transfer():\n    to=request.args.get('to')\n    amt=request.args.get('amt')\n    db.execute(\"INSERT INTO transfers(from_user,to_user,amount)VALUES(?,?,?)\",(current_user.id,to,amt))\n    return 'ok'","@app.route(\"/api/transfer\",methods=[\"POST\"])\ndef transfer():\n    to=request.form.get('to')\n    amt=request.form.get('amt')\n    if request.form.get('csrf')!=session.get('csrf'): abort(403)\n    db.execute(\"INSERT INTO transfers(from_user,to_user,amount)VALUES(?,?,?)\",(current_user.id,to,amt))\n    return 'ok'"),
    # Security Java (+1)
    ("java","@PostMapping(\"/api/register\")ResponseEntity<?>register(@RequestBody User u){userRepo.save(u);return ResponseEntity.ok().build()}","@PostMapping(\"/api/register\")ResponseEntity<?>register(@RequestBody @Valid RegisterDto dto){User u=new User();u.setName(dto.getName());u.setEmail(dto.getEmail());u.setPassword(passwordEncoder.encode(dto.getPassword()));userRepo.save(u);return ResponseEntity.ok().build()}"),
]
for l,bad,good in pairs_final3:
    S(f"```{l}\n{bad}\n```",f"Guvenlik acigi var. Cozumu:\n```{l}\n{good}\n```",l)
print(f"After security extras: {len(D)}")

pairs_ref5 = [
    # Refactoring Python (+26)
    ("python","data=get_from_api()\nitems=[]\nfor d in data:\n    if d['status']=='active':\n        items.append({'id':d['id'],'name':d['name']})","data=get_from_api()\nitems=[{'id':d['id'],'name':d['name']}for d in data if d['status']=='active']"),
    ("python","def is_valid(s):\n    if s and len(s.strip())>0:\n        return True\n    return False","def is_valid(s): return bool(s and s.strip())"),
    ("python","def get_first(items):\n    if len(items)>0:\n        return items[0]\n    return None","def get_first(items): return items[0] if items else None"),
    ("python","class Rectangle:\n    def __init__(self,w,h):\n        self.w=w\n        self.h=h\n    def area(self):\n        return self.w*self.h","class Rectangle:\n    def __init__(self,width,height):\n        self.width=width\n        self.height=height\n    @property\n    def area(self):\n        return self.width*self.height"),
    ("python","class Shape:\n    def area(self):pass\nclass Circle(Shape):\n    def __init__(self,r):self.r=r\n    def area(self):return 3.14*self.r*self.r\nclass Rect(Shape):\n    def __init__(self,w,h):self.w=w;self.h=h\n    def area(self):return self.w*self.h","from abc import ABC,abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):pass\nclass Circle(Shape):\n    def __init__(self,radius):self.radius=radius\n    def area(self):return 3.14*self.radius**2\nclass Rect(Shape):\n    def __init__(self,width,height):self.width=width;self.height=height\n    def area(self):return self.width*self.height"),
    ("python","def format_date(d):return d.strftime('%Y')+'/'+d.strftime('%m')+'/'+d.strftime('%d')","def format_date(d):return d.strftime('%Y/%m/%d')"),
    ("python","def parse_config():\n    with open('config.yaml') as f:\n        config=yaml.safe_load(f)\n    host=config.get('database',{}).get('host','localhost')\n    port=config.get('database',{}).get('port',5432)\n    return f'{host}:{port}'","def parse_config():\n    with open('config.yaml') as f:\n        config=yaml.safe_load(f)\n    db=config.get('database',{})\n    host=db.get('host','localhost')\n    port=db.get('port',5432)\n    return f'{host}:{port}'"),
    ("python","class User:\n    def __init__(self,d):\n        self.first=d['first']\n        self.last=d['last']\n        self.full=self.first+' '+self.last","class User:\n    def __init__(self,d):\n        self.first=d['first']\n        self.last=d['last']\n    @property\n    def full(self):return f'{self.first} {self.last}'"),
    ("python","a=10;b=20;c=30;d=40;e=50\ntotal=a+b+c+d+e","total=sum([10,20,30,40,50])"),
    ("python","data=[]\nfor i in range(100):\n    data.append(i*i)","data=[i*i for i in range(100)]"),
    ("python","def get_data():\n    import json\n    with open('data.json') as f:\n        return json.load(f)","import json\ndef get_data():\n    with open('data.json') as f:\n        return json.load(f)"),
    ("python","text='';lines=[]\nfor line in open('file.txt'):\n    text+=line\n    lines.append(line.strip())","lines=[line.strip()for line in open('file.txt')]\ntext='\\n'.join(lines)"),
    ("python","def dbg(msg):print(f'[DEBUG] {msg}')\ndef info(msg):print(f'[INFO] {msg}')\ndef err(msg):print(f'[ERROR] {msg}')","import logging\nlogging.basicConfig(level=logging.INFO)\nlog=logging.getLogger(__name__)\ndef dbg(m):log.debug(m)\ndef info(m):log.info(m)\ndef err(m):log.error(m)"),
    ("python","def to_ints(strings):\n    result=[]\n    for s in strings:\n        result.append(int(s))\n    return result","def to_ints(strings):return list(map(int,strings))"),
    ("python","set1=set(a for a,b in pairs)\nset2=set(b for a,b in pairs)","set1,set2=map(set,zip(*pairs)) if pairs else (set(),set())"),
    ("python","if isinstance(x,int):\n    if x>0:print('positive')\n    else:print('non-positive')\nelse:print('not int')","if isinstance(x,int):\n    print('positive' if x>0 else 'non-positive')\nelse:print('not int')"),
    ("python","def toggle(flag):\n    if flag:\n        return False\n    else:\n        return True","def toggle(flag):return not flag"),
    ("python","if a==None: a=[]\nif b==None: b={}\nif c==None: c=''","a=a or [];b=b or {};c=c or ''"),
    ("python","d={'a':1,'b':2}\nfor k in d:\n    v=d[k]\n    print(k,v)","for k,v in d.items():print(k,v)"),
    ("python","def find_max(items):\n    m=items[0]\n    for i in range(1,len(items)):\n        if items[i]>m:m=items[i]\n    return m","return max(items) if items else None"),
    ("python","import os, shutil\ndef backup(src,dst):\n    for f in os.listdir(src):\n        shutil.copy(os.path.join(src,f),dst)","import shutil\ndef backup(src,dst):shutil.copytree(src,dst,dirs_exist_ok=True)"),
    ("python","count=0\nfor i in range(100):\n    if i%3==0:count+=1","count=len([i for i in range(100)if i%3==0])"),
    ("python","start=time.time()\ndo_work()\nend=time.time()\nprint(end-start)","from time import perf_counter\nstart=perf_counter()\ndo_work()\nprint(perf_counter()-start)"),
    ("python","def factorial(n):\n    result=1\n    for i in range(2,n+1):\n        result*=i\n    return result","import math\ndef factorial(n):return math.factorial(n)"),
    ("python","def wait(seconds):\n    import time\n    time.sleep(seconds)","from time import sleep\ndef wait(seconds):sleep(seconds)"),
    ("python","d={}\nfor i,item in enumerate(items):\n    d[i]=item","d=dict(enumerate(items))"),
]
for l,bad,good in pairs_ref5:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)
print(f"After ref5: {len(D)}")

pairs_ref6 = [
    # Refactoring JavaScript (+30)
    ("javascript","var result = 0;\nfor(var i = 0; i < nums.length; i++){\n    result += nums[i];\n}","const result = nums.reduce((a,b)=>a+b,0)"),
    ("javascript","function User(name, age){this.name=name;this.age=age}\nUser.prototype.greet=function(){return 'Hi '+this.name}","class User{\n  constructor(name,age){this.name=name;this.age=age}\n  greet(){return `Hi ${this.name}`}\n}"),
    ("javascript","var fs = require('fs');\nvar data = fs.readFileSync('f.txt','utf8');\nvar lines = data.split('\\n');","const fs = require('fs/promises');\nasync function readLines(){\n  const data = await fs.readFile('f.txt','utf8');\n  return data.split('\\n');\n}"),
    ("javascript","function findById(items, id){\n    for(var i=0; i<items.length; i++){\n        if(items[i].id === id) return items[i];\n    }\n    return null;\n}","function findById(items, id){ return items.find(item => item.id === id) ?? null; }"),
    ("javascript","function User(name, role){\n    this.name = name;\n    this.role = role || 'user';\n}","function User(name, role = 'user'){\n    this.name = name;\n    this.role = role;\n}"),
    ("javascript","const result = [];\nfor(let i = 0; i < arr.length; i++){\n    if(arr[i].active){\n        result.push({id: arr[i].id, name: arr[i].name});\n    }\n}","const result = arr.filter(x => x.active).map(x => ({id: x.id, name: x.name}))"),
    ("javascript","document.querySelectorAll('.item').forEach(function(el){\n    el.classList.add('highlight');\n});","document.querySelectorAll('.item').forEach(el => el.classList.add('highlight'))"),
    ("javascript","const name = user.name ? user.name : 'Guest';","const name = user.name || 'Guest'"),
    ("javascript","const xhr = new XMLHttpRequest();\nxhr.open('GET', '/api/data');\nxhr.onload = function(){ console.log(xhr.responseText); };\nxhr.send();","fetch('/api/data').then(r => r.text()).then(console.log)"),
    ("javascript","function save(name, value){\n    if(typeof(Storage) !== 'undefined'){\n        localStorage.setItem(name, value);\n    }\n}","function save(name, value){\n    try { localStorage.setItem(name, value); } catch(e) {}\n}"),
    ("javascript","const age = parseInt(prompt('Enter age'));\nif(age >= 18 && age <= 65){\n    console.log('working age');\n}","const age = parseInt(prompt('Enter age'));\nif(age >= 18 && age <= 65) console.log('working age');"),
    ("javascript","const items = [1, 2, 3, 4, 5];\nconst doubled = [];\nitems.forEach(function(n){\n    doubled.push(n * 2);\n});","const items = [1, 2, 3, 4, 5];\nconst doubled = items.map(n => n * 2);"),
    ("javascript","const result = some ? true : false;","const result = !!some;"),
    ("javascript","function getQueryParam(name){\n    const url = window.location.search;\n    const params = new URLSearchParams(url);\n    return params.get(name);\n}","function getQueryParam(name){ return new URLSearchParams(location.search).get(name); }"),
    ("javascript","const req = require('http').request(options, function(res){\n    let data = '';\n    res.on('data', chunk => data += chunk);\n    res.on('end', () => console.log(data));\n});\nreq.end();","const fetch = require('node-fetch');\nfetch(options).then(r => r.text()).then(console.log);"),
    ("javascript","function isAdult(age){ if(age >= 18) return true; else return false; }","function isAdult(age){ return age >= 18; }"),
    ("javascript","console.log('User: ' + name + ', Age: ' + age);","console.log(`User: ${name}, Age: ${age}`);"),
    ("javascript","const arr = [1, 2, 3];\nfor(let i in arr){ console.log(arr[i]); }","for(let v of arr){ console.log(v); }"),
    ("javascript","const users = [\n    {name: 'Ali', scores: [80,90,70]},\n    {name: 'Veli', scores: [85,95,75]}\n];\nusers.forEach(function(u){\n    let total = 0;\n    u.scores.forEach(function(s){ total += s; });\n    console.log(u.name, total / u.scores.length);\n});","users.forEach(u => {\n    const avg = u.scores.reduce((a,b)=>a+b,0) / u.scores.length;\n    console.log(u.name, avg);\n});"),
    ("javascript","function doSomething(callback){\n    setTimeout(function(){\n        callback('done');\n    }, 1000);\n}","function doSomething(){\n    return new Promise(resolve => setTimeout(() => resolve('done'), 1000));\n}"),
    ("javascript","const copy = JSON.parse(JSON.stringify(obj));","const copy = structuredClone(obj);"),
    ("javascript","const http = require('http');\nconst app = http.createServer((req,res)=>{ res.end('ok'); });\napp.listen(3000);","const express = require('express');\nconst app = express();\napp.get('/', (req,res) => res.send('ok'));\napp.listen(3000);"),
    ("javascript","function getFirst(arr){ if(arr && arr.length > 0) return arr[0]; return null; }","function getFirst(arr){ return arr?.[0] ?? null; }"),
    ("javascript","for(var i=0;i<10;i++){ (function(i){ setTimeout(function(){ console.log(i); }, i*100); })(i); }","for(let i=0;i<10;i++){ setTimeout(() => console.log(i), i*100); }"),
    ("javascript","var app = require('express')();\nvar bodyParser = require('body-parser');\napp.use(bodyParser.json());","import express from 'express';\nimport { json } from 'body-parser';\nconst app = express();\napp.use(json());"),
    ("javascript","const express = require('express');\nconst router = express.Router();\nrouter.get('/users', (req,res)=>res.json([]));","const {Router} = require('express');\nconst router = Router();"),
    ("javascript","axios.get('/api/users').then(function(resp){\n    const users = resp.data;\n    users.forEach(function(u){ console.log(u.name); });\n});","const {data: users} = await axios.get('/api/users');\nusers.forEach(u => console.log(u.name));"),
    ("javascript","const arr = [0, null, undefined, '', false, 1, 2];\nconst filtered = arr.filter(function(x){ return x; });","const filtered = arr.filter(Boolean);"),
    ("javascript","const arr = [1,2,3,4,5];\nconst evens = [];\nfor(let i=0;i<arr.length;i++){\n    if(arr[i]%2===0) evens.push(arr[i]);\n}","const evens = arr.filter(x => x%2===0);"),
    ("javascript","function sum(){\n    var total = 0;\n    for(var i=0;i<arguments.length;i++){\n        total += arguments[i];\n    }\n    return total;\n}","function sum(...nums){\n    return nums.reduce((a,b)=>a+b,0);\n}"),
    # Refactoring Java (+10)
    ("java","public List<String> getActiveNames(List<User> users){\n    List<String> names = new ArrayList<>();\n    for(User u : users){\n        if(u.isActive()) names.add(u.getName());\n    }\n    return names;\n}","public List<String> getActiveNames(List<User> users){\n    return users.stream().filter(User::isActive).map(User::getName).toList();\n}"),
    ("java","if(list != null && list.size() > 0){\n    return list.get(0);\n}","if(list != null && !list.isEmpty()){\n    return list.get(0);\n}"),
    ("java","public String capitalize(String s){\n    if(s == null || s.isEmpty()) return s;\n    return s.substring(0,1).toUpperCase() + s.substring(1);\n}","public String capitalize(String s){\n    if(s == null || s.isEmpty()) return s;\n    return Character.toUpperCase(s.charAt(0)) + s.substring(1);\n}"),
    ("java","public boolean isNullOrEmpty(String s){\n    if(s == null) return true;\n    if(s.length() == 0) return true;\n    return false;\n}","public boolean isNullOrEmpty(String s){ return s == null || s.isEmpty(); }"),
    ("java","public String join(List<String> items, String delimiter){\n    StringBuilder sb = new StringBuilder();\n    for(int i=0; i<items.size(); i++){\n        if(i>0) sb.append(delimiter);\n        sb.append(items.get(i));\n    }\n    return sb.toString();\n}","public String join(List<String> items, String delimiter){\n    return String.join(delimiter, items);\n}"),
    ("java","@GetMapping(\"/items\")public ResponseEntity<List<Item>> getItems(@RequestParam(defaultValue=\"0\")int page,@RequestParam(defaultValue=\"20\")int size){return ResponseEntity.ok(itemService.findAll(page,size));}","@GetMapping(\"/items\")public ResponseEntity<Page<Item>> getItems(@PageableDefault Pageable p){return ResponseEntity.ok(itemService.findAll(p));}"),
    ("java","public int parseIntOrDefault(String s, int def){\n    try{\n        return Integer.parseInt(s);\n    }catch(NumberFormatException e){\n        return def;\n    }\n}","public int parseIntOrDefault(String s, int def){\n    try{ return Integer.parseInt(s); }\n    catch(NumberFormatException e){ return def; }\n}"),
    ("java","public User createUser(String name, String email){\n    User u = new User();\n    u.setName(name);\n    u.setEmail(email);\n    return userRepo.save(u);\n}","public User createUser(String name, String email){\n    return userRepo.save(new User(name, email));\n}"),
    ("java","String result = \"\";\nfor(String s : list){\n    if(result.length() > 0) result += \",\";\n    result += s;\n}","String result = String.join(\",\", list);"),
    ("java","public void notifyUsers(List<User> users, String msg){\n    for(User u : users){\n        sendEmail(u.getEmail(), msg);\n    }\n}","public void notifyUsers(List<User> users, String msg){\n    users.parallelStream().forEach(u -> sendEmail(u.getEmail(), msg));\n}"),
]
for l,bad,good in pairs_ref6:
    R(f"```{l}\n{bad}\n```",f"```{l}\n{good}\n```",l)
print(f"After ref6: {len(D)}")

# Final write
with open(O,"w",encoding="utf-8") as f:
    json.dump(D,f,ensure_ascii=False,indent=2)
print(f"FINAL written: {len(D)} pairs")
