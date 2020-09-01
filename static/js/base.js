var parseQuery = function(queryString) {
  var query = {};
  var pairs = (queryString[0] === '?' ? queryString.substr(1) : queryString).split('&');
  for (var i = 0; i < pairs.length; i++) {
      var pair = pairs[i].split('=');
      query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
  }
  return query;
}
var loadForm = function (url, modal_size) {
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
      if (typeof(form_init_js) == "function") {
        form_init_js(this.url);
      }
    }
  });
}

var saveForm = function (event) {
  event.preventDefault();
  var form = $(this);
  var modal_size = $(this).attr("class").split("-")[3];
  var formData = new FormData(this);
  $.ajax({
    url: form.attr("action"),
    data: formData,
    type: form.attr("method"),
    dataType: 'json',
    processData: false,
    contentType: false,
    success: function (data) {
      if (data.form_is_valid == undefined) {
        location.reload();
      }
      else {
        if (data.form_is_valid) {
          if (location.href.endsWith('/crud/read')) {location.href = data.content_list;}
          else {location.reload();}
        }
        else {
          $("#modal-div-" + modal_size + " .modal-content").html(data.html_form);
        }
      }
    }
  });
  return false;
};

var closeForm = function() {
  var form = $(this);
  var modal_size = $(this).attr("class").split("-")[3];
  $("#modal-div-" + modal_size + " .modal-content").html("")
};

var initializeOptArray = function(app_id, url_prefix) {
  this[app_id + "url_prefix"] = url_prefix;
  this[app_id + "optArray"] = [];
  this[app_id + "optObject"] = new Object();
  this[app_id + "optCheckedCount"] = 0;
}

var checkOrUncheckAll = function(app_id, checked) {
  var items = this[app_id + "optObject"];
  for (item in items) {
    document.getElementById("opt_" + item).checked = checked;
    updateOptArray(app_id, item, checked);
  }
  if (!checked) {this[app_id + "optCheckedCount"] = 0;}
}

var submit_with_returnURL = function(target_url, isSourceURL) {
  // Rebuild current url without pu_url
  var parms = parseQuery(location.search);

  su_url_from_current_url = "";
  if (parms.su_url != undefined) {su_url_from_current_url = parms.su_url;}
  if (target_url == su_url_from_current_url) {
    location.href = target_url;
  }
  else {
    current_url = ""
    for (parm in parms) {
      if (parm != "pu_url") {
        if (current_url.length > 0) {current_url = current_url + "&"}
        else {current_url = current_url + "?"}
        current_url = current_url + parm + "=" + parms[parm];
      }
    }
    current_url = location.pathname + current_url;

    // Extract teh target_path and target_search to prep for target_url rebuild
    target_pathname = target_url;
    target_search = "";
    if (target_url.indexOf("?") > -1) {
      target_pathname = target_url.substr(0, target_url.indexOf("?"));
      target_search = target_url.substr(target_url.indexOf("?"), target_url.length)
    }

    // Rebuild the target_url by taking on the current_url and source_url
    parms = parseQuery(target_search);
    parms.pu_url = encodeURIComponent(current_url);
    if (isSourceURL) {parms.su_url = encodeURIComponent(current_url);}
    else {
      if (su_url_from_current_url.length > 0) {parms.su_url = encodeURIComponent(su_url_from_current_url);}
    }
    urlString = "";
    for (parm in parms) {
      if (parm != target_pathname) {
        if (urlString.length > 0) {urlString = urlString + "&"}
        else {urlString = urlString + "?"}
        urlString = urlString + parm + "=" + parms[parm];
      }
    }

    location.href = target_pathname + urlString
  }
}

single_href_option = function(url) {
  selected_input = $("input[name^='opt']:checked");
  if (selected_input.length == 0) {
    alert('No items have been selected yet.');
  }
  else {
    if (selected_input.length > 1) {
        alert('Multiple items cannot be checked for this action.');
    }
    else {
      try {url = url.replace("--slug--", selected_input[0].getAttribute("slug"))} catch(e) {}
      try {url = url.replace("--pk--", selected_input[0].getAttribute("pk"))} catch(e) {}
      location.href = url
    }
  }
}

single_modal_option = function(url, modal_size) {
  selected_input = $("input[name^='opt']:checked");
  if (selected_input.length == 0) {
    alert('No item has been selected yet.');
  }
  else {
    if (selected_input.length > 1) {
      alert('Only one item can be selected.');
    }
    else {
      try {url = url.replace("--slug--", selected_input[0].getAttribute("slug"))} catch(e) {}
      try {url = url.replace("--pk--", selected_input[0].getAttribute("pk"))} catch(e) {}
      loadForm(url, modal_size);
    }
  }
}

multiple_modal_option = function(url, modal_size) {
  selected_input = $("input[name^='opt']:checked");
  if (selected_input.length == 0) {
    alert('No items have been selected yet.');
  }
  else {
    var multList = "";
    for (i = 0; i < selected_input.length; i++) {
      if (multList.length > 0) {multList = multList + ":"}
      multList = multList + selected_input[i].getAttribute("pk");
    }
    loadForm(url + '?multlist=' + multList, modal_size);
  }
}

dual_modal_option = function(single_url, multiple_url, modal_size) {
  selected_input = $( "input:checked" );
  if (selected_input.length == 0) {
    alert('No items have been selected yet.');
  }
  else {
    if (selected_input.length > 1) {
      var multList = "";
      for (i = 0; i < selected_input.length; i++) {
        if (multList.length > 0) {multList = multList + ":"}
        multList = multList + selected_input[i].getAttribute("pk");
      }
      loadForm(multiple_url + '?multlist=' + multList, 'lg');
    }
    else {
      try {single_url = single_url.replace("--slug--", selected_input[0].getAttribute("slug"))} catch(e) {}
      try {single_url = single_url.replace("--pk--", selected_input[0].getAttribute("pk"))} catch(e) {}
      loadForm(single_url, modal_size);
    }
  }
}
