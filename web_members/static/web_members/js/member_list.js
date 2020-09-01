var saveFilterForm = function () {
  var form = $(this);
  var modal_size = "cf";
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid == undefined) {
        location.reload();
      }
      else {
        if (data.form_is_valid) {
          location.href = data.queryString;
        }
        else {
          $("#modal-div-" + modal_size + " .modal-content").html(data.html_form);
        }
      }
    }
  });
  return false;
};
var loadFilterForm = function (url, modal_size) {
  $.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal-div-" + modal_size + " .modal-content").html("");
      $("#modal-div-" + modal_size).modal("show");
    },
    success: function (data) {
      $("#modal-div-" + modal_size + " .modal-content").html(data.html_form);
    }
  });
}
