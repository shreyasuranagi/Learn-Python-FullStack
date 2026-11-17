let userinfo = {
    name: 'shreya',
    isLoggedIn: true,
    streak:7,
    days:360,
    subjects: ['js','html','pyton','sql'],
    status: 'busy',

    coding: function(){
        console.log(name,'is coding now');
    },
    resting: (name) => { console.log(name,'is resting');},

    eating: function eat(){ console.log('eating...');
    }
}

console.log(userinfo);

/*
objects are a programmmatical representation of a real world entity whose properties i.e., state and behaviours are represeneted as a key - value pairs
*/

/*
create 