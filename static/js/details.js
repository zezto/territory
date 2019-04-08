$(document).ready(function () {
    let select;
    let idd
    $('a').on('click', function (event) {
        idd = Number(event.target.id);
        select = '.bg-modal' + idd
        $(select).toggleClass('active')
        $(select).show()
    });
    $('.btn').on('click', function () {
        $(select).hide()
        $(select).toggleClass('active')
        select = ''
    });
    $('.detail-form').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
    function create_post() {
        console.log("create post is working!") // sanity check
        var pathway = location.pathname
        var kek = '#info' + idd
        var result = '#post-result' + idd
        var real_deal = $(kek).html()
        var form_ifno = $(`form#post-form${idd} input[type=text]`)
        let lol = new Object
        for (let index = 0; index < form_ifno.length; index++) {
            var keku = form_ifno[index]['value']
            lol[index] = keku
        }
        let emptyness = 0
        for (var jnj in lol) {
            if (lol[jnj].length == 0) {
                emptyness++
            }
        }
        var results = JSON.stringify(lol)
        if (emptyness == 4) {
            $(result + ' .empty').show(3).delay(3000).hide(3);
        }
        else {
            $.ajax({
                url: pathway + "create_post", // the endpoint
                type: "POST", // http method
                data: { number: real_deal, idd, results }, // data sent with the post request

                // handle a successful response
                success: function (json) {
                    $(result + ' .good').show(3).delay(3000).hide(3); // remove the value from the input
                    console.log(json); // log the returned json to the console
                    console.log("success"); // another sanity check
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    $('.bad').toggleClass()
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        }
    };
    $('#terr-options').on('click', () => {
        $('.options').toggleClass('active')
        $('.options').toggle();
    });
    $('#options-close').on('click', () => {
        $('.options').toggleClass('active')
        $('.options').toggle();

    });
    $('#add-street').on('click', () => {
        $('#street-add').toggle();
    });
    $('#street-add-form').on('submit', (event) => {
        event.preventDefault();
        addstreet()
    })
    function addstreet() {
        let pk = $('#terr-pk').html()
        let extract = $('form#street-add-form input[type=text]')
        let streetName = extract[0]['value']
        let pathway = location.pathname
        if (streetName.length == 0) {
            $('.empty').show(3).delay(3000).hide(3);
        }
        else {
            $.ajax({
                url: pathway + "add-street",
                type: 'POST',
                data: { pk, streetName },

                success: (json) => {
                    console.log(json)
                    $('.good').show(3).delay(3000).hide(3);
                },

                error: (xhr, errmsg, err) => {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            })
        }
    };
    let current;
    let pk;
    let nummodal;
    let fd;
    $('.number-add').on('click', function (event) {
        current = event.target.id
        pk = current.slice(3)
        nummodal = '.num-options' + pk
        $(nummodal).toggleClass('active')
        $(nummodal).toggle()
    });
    $('.close-btn').on('click', () => {
        $(nummodal).toggleClass('active')
        $(nummodal).toggle();
    });
    $('[id=add-number]').on('click', () => {
        let lel = '#num-add' + pk;
        $(lel).toggle();
    });
    $('.test button[type=submit]').on('click', (event) => {
        event.preventDefault();
        addNumber();
    })
    function addNumber() {
        let testerr = '#number-add-box' + pk
        let numberValue = $(testerr).val();
        console.log(numberValue)
        let pathway = location.pathname
        let pather = '.unq'
        if (numberValue.length == 0) {
            $('.empty').show(3).delay(3000).hide(3);
        }
        else {
            $.ajax({
                url: pathway + "add-number",
                type: 'POST',
                data: { pk, numberValue },

                success: (json) => {
                    console.log(json)
                    $(pather).show()
                    $('.good').show(3).delay(3000).hide(3);
                },

                error: (xhr, errmsg, err) => {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            })
        }
    }
});
