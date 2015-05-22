/**
 * Created by lee on 2015/4/29.
 */
$(function () {
    $("#set").click(
        function () {
            var name = $.trim($("#name").val());
            var age = $.trim($("#age").val());
            var address = $.trim($("#address").val());
            $.get("/ms_save/", {
                    'name': name,
                    'age': age,
                    'address': address
                },
                function (jsons) {
                    alert(jsons.message)
                    window.location.reload()
                })
        }
    )
});

function deletes(ide) {
    $.get("/delete/", {
            'id': ide
        },
        function (jsons) {
            alert(jsons.message)
            window.location.reload()
        })
}

function update(ide) {
    var name = $.trim($("#rname_"+ide).val());
    var age = $.trim($("#rage_"+ide).val());
    var address = $.trim($("#raddress_"+ide).val());
    $.get("/update/", {
            'id': ide,
            'name': name,
            'age': age,
            'address': address
        },
        function (jsons) {
            alert(jsons.message)
            window.location.reload()
        })
}