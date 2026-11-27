//!cafe


function orderfood(callback) {
    setTimeout(() => {
        console.log('your fav food is ordered!!');
    }, 2000)
    callback()
}


function preparefood(callback) {
    setTimeout(() => {
        console.log('done preparing food');
    }, 2000) // doesnt work in order if given 5000
    callback()
}


function payment(calback) {
    setTimeout(() => {
        console.log('payment is dont');

    }, 2000);
    calback()
}


function takeaway(callback) {
    setTimeout(() => {
        console.log('ready for takeaway!');
        callback()
    }, 2000)

}


orderfood(() => {
    preparefood(() => {
        payment(() => {
            takeaway(() => {
                console.log('Enjoy your food!');
            });
        });
    });
});


//
// your fav food is ordered!!
// done preparing food
// ready for takeaway!
// Enjoy your food!




// your fav food is ordered!!
// done preparing food
// payment is dont
// ready for takeaway!
// Enjoy your food!