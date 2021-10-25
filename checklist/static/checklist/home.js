// AJAX search objects
const search_input = $('#search-input');
const search_filter = $('.search-filter');
const pokelist_div = $('#replaceable-content');
const endpoint = '/ajax/change_status';
const delay_by_in_ms = 700;
let scheduled_function = false;

// Other variables
const stat_change = $('.stat-change'); 
const card_sprite = document.getElementById('sprite');
const card_sprite_shiny = document.getElementById('sprite-shiny');



// Sends the request parameters to the endpoint (see urls.py)
let ajax_call = function(endpoint, request_parameters)
{
    $.getJSON(endpoint, request_parameters)
        .done(response => 
            {
                pokelist_div.html(response['html_from_view']); // replace html contents
            });
}

// Realtime search bar
search_input.on('keyup', function()
{
    const request_parameters = { 
        q: $(this).val() // The user input/search query
    }
    
    if(scheduled_function)
    {
        clearTimeout(scheduled_function);
    }
    
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters);
});

// Search Filters
search_filter.on('change', function(e)
{
    e.stopImmediatePropagation();

    if(this.type == "checkbox")
    {
        request_parameters = {
            filter: this.id,
            value: this.checked
        }
    }
    else
    {
        request_parameters = {
            filter: this.id,
            value: $(this).val(),
        }
    }

    ajax_call(endpoint, request_parameters);
});

// Change status 
stat_change.on('change', function()
{    
    pokeballs = $('.caught-pokeballs')
    
    if(this.type == "checkbox")
    {
        request_parameters = {
            dexid: this.name,
            status_change: this.id,
            value: this.checked
        }
    }
    else
    {
        request_parameters = {
            dexid: this.name,
            status_change: this.id,
            value: $(this).val(),
        }
    }
        
    if(this.id == "caught" || this.id == "caught-shiny" || this.classList.contains('caught-pokeballs'))
    {
        GrayscaleToggle(this.id, this.checked);
    }
    
    ajax_call(endpoint, request_parameters);
});
    
let GrayscaleToggle = function(object_id, checked_status)
{     
    var object = document.getElementById(object_id);
    
    if(object_id == "caught")
    {
        if(checked_status == 1)
        {
            card_sprite.style.filter = "grayscale(0%)";
        }
        else
        {
            card_sprite.style.filter = "grayscale(100%)";
        }
    }
    
    else if(object_id == "caught-shiny")
    {
        
        if(checked_status == 1)
        {
            card_sprite_shiny.style.filter = "grayscale(0%)";
        }
        else
        {
            card_sprite_shiny.style.filter = "grayscale(100%)";
        }
    }
    
    else
    {
        if(checked_status == 1)
        {
            object.labels[0].style.filter = "grayscale(0%)";
        }
        else
        {
            object.labels[0].style.filter = "grayscale(100%)";
        }
    }
};

// For future implementation
// $(window).scroll(function() 
// {
//     if($(window).scrollTop() == $(document).height() - $(window).height()) {

//         const cards = $('.card').length;

//         request_parameters = {
//             load_limit: cards
//         }

//         console.log("sent")

//         ajax_call(endpoint, request_parameters);
//     }
// });



