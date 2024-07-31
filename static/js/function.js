console.log("working Fine");

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data:$(this).serialize(),
        method:$(this).attr("method"),
        url:$(this).attr("action"),
        dataType:"json",
        success:function(response){
            console.log("comment saved to DB")
            if(response.bool==true){
                $("#review-rsp").html("Review added successuflly.")
                
            }
        }
    })
})