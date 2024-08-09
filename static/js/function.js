console.log("working Fine");

const monthNames = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];

$("#commentForm").submit(function (e) {
    e.preventDefault();
    let dt = new Date();
    let time = dt.getDay() + " " + monthNames[dt.getUTCMonth] + "," + dt.getFullYear();

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function (res) {
            console.log("comment saved to DB")
            if (res.bool == true) {
                $("#review-rsp").html("Review added successuflly.").show();
                $(".hide-comment-form").hide();

                let_html = ' <div class="product__details__tab__desc">'
                _html += '<div class="review-content">'
                _html += ' <img src="https://t4.ftcdn.net/jpg/00/64/67/27/360_F_64672736_U5kpdGs9keUll8CRQ3p3YaEv2M6qkVY5.jpg" alt="" class="user-img"/>'

                _html += ' <div class="review-text">'
                _html += ' <span class="font-xs text-muted">' + time + '</span>'
                _html += '<h6>' + res.context.user + '</h6>'

                for (let i = 1; i <= res.context.review; i++)(
                    _html += '<i class="fas fa-star text-warning"></i>'
                )
                _html += '<p>' + res.context.review + '</p>'
                _html += '</div>'

                _html += '<div class="average-rating-reviews">'
                _html += '<span>Average rating: {{average_rating.rating|floatformat}} out of 5</span>'
                _html += '</div>'
                _html += '</div>'
                _html += '</div>'
                $(".comment-list").prepend(_html)
            }

        }
    })
})

$(document).ready(function () {
    $(".filter-checkbox").on("click", function () {
        console.log("A checkbox have been clicked");
        let filter_object = {}
        $(".filter-checkbox").each(function () {
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function (element) { return element.value })
        })
        console.log("Filter object is :", filter_object);
    })
})