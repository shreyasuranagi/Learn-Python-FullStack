```
.centermain{
    padding:10px 10px;
    display:flex;
    flex-direction:column;
    justify-content:space-around;
    align-items: start;
    gap:15px;
    flex-shrink:0;
    overflow-y:scroll;
}
.outer{
flex-basis:100px;

}
.row{
    background-color: blue;
    display:flex;
    flex-direction:row;
    justify-content: space-between;
    gap:30px;
    /* flex-basis:100px; */
    overflow-x:scroll;
    flex-wrap:nowrap;
    flex-shrink:0;
}

.box{
    width:150px;
    height:150px;
    background-color: white;
    border:2px solid red;
    flex-shrink:0;
}
```

### miistakes and takeaways

- overflow:scroll sets on both x and y not necessary. can be done using overflow:auto/ overflow-x:auto for the .row
- for scrollbale rows best to go with jsutify-content:flex-start instead of space-between becuase the latter making the scroll track disappear
- why the rows were shrinking: cos flex-shrink:1 by default on the flex items(box and rows). Also give it for all the containers
- align-items:stretch instead of flex-start cos flex-start 