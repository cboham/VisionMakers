function detail_type(sku){
  window.location = "frame-type/" + sku + "/";
}


function display(num){

  // reset all rows
  var table = document.getElementById("bodytable");
  var rows = table.rows.length;

  for (var i = 1; i <= rows; i = i + 1){
    if (i!= num){
    document.getElementById('row' + String(i)).style.background = "#fff";
    //console.log(i);
    }
  }
  /*
  *for.loop counter starts at 1 not zero
  */
  document.getElementById('row' + String(num)).style.background = "#949494";
  document.getElementById('row' + String(num)).value = "true";


  buildHTML(num);
  var sku = document.getElementById('sku').value;
  //Display the delete button
  var form = document.getElementById('delete-form');
  var input = document.getElementById('delete-input');
  form.style = "display:inline;";
  form.action = "/inventory/frame-type/" + document.getElementById('sku').value + "/delete/";
  input.value = document.getElementById('sku').value;

  var button = document.getElementById('edit-button');
  button.style = "display:inline;";
  button.setAttribute("href",  "/inventory/frame-type/" + document.getElementById('sku').value + "/edit/")
  //button.setAttribute("onclick", "edit(" + document.getElementById('sku').value + ")");


  var form = document.getElementById('print-form');
  var input = document.getElementById('print-input');
  form.style = "display:inline;";
  form.href = "/inventory/frame-type/" + document.getElementById('sku').value + "/print/";


  for (var i = 1; i <= rows; i = i + 1){
    if (i!= num){
    document.getElementById('pair_set_' + String(i)).style= "display:none";
    //console.log(i);
    }
  }
  var table = document.getElementById('pair_set_' + num);
  table.style = "display:block"
}

function edit(sku){
  //console.log(1);
  var inputs = document.getElementsByClassName('form-control');
  // for (var i = 0; i < inputs.length; i++){
  //   if(i < 11 || i > 14){
  //     inputs[i].readOnly = false;
  //     //taxable needs to be changed to a checkbox
  //   }
  // }

  //document.getElementById('navbar').style = "display:none";

  //var windowFeatures = 'noopener = true, toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes, height = 300, width = 800 left = 200, top = 150';
  //var win = window.open("/inventory/frame-type/" + sku + "/edit/", "Edit Frame", windowFeatures);


}

/*
function hover(num){
  var rows = document.getElementById("mytable").rows.length - 1;
  console.log(selected);
  for (var i = 1; i <= rows; i = i + 1){
    var selected = document.getElementById('row' + String(num)).value;
    if (i!= num && selected != "true"){
      document.getElementById('row' + String(i)).style.background = "#949494";
    }
  }
  document.getElementById('row' + String(num)).style.background = "#fff";
}
*/

function buildHTML(num){

  var table = document.getElementById("bodytable");
  html = table.rows[num - 1].cells.item(0).innerHTML;
  document.getElementById('sku').value = html;

  html = table.rows[num - 1].cells.item(1).innerHTML;
  document.getElementById('desc').value = html;

  html = table.rows[num - 1].cells.item(2).innerHTML;
  document.getElementById('vendor').value = html;

  html = table.rows[num - 1].cells.item(3).innerHTML;
  if (html == 'M'){
    html = "Men's";
  } else{
    html = "Women's";
  }
  document.getElementById('style').value = html;

  html = table.rows[num - 1].cells.item(4).innerHTML;
  document.getElementById('retail').value = html;

  /* hidden table values */
  html = document.getElementById('hidden-table').rows[num].cells.item(0).innerHTML;
  document.getElementById('comments').value = html;

  html = document.getElementById('hidden-table').rows[num].cells.item(1).innerHTML;
  document.getElementById('on_hand_bv').value = html;

  html = document.getElementById('hidden-table').rows[num].cells.item(2).innerHTML;
  document.getElementById('on_hand_wd').value = html;

  html = document.getElementById('hidden-table').rows[num].cells.item(3).innerHTML;
  document.getElementById('on_hand_pa').value = html;
  /* end hiddn table alues */

  html = table.rows[num - 1].cells.item(6).innerHTML;
  document.getElementById('color').value = html;

  html = table.rows[num - 1].cells.item(7).innerHTML;
  document.getElementById('locations').value = html;

  html = table.rows[num - 1].cells.item(8).innerHTML;
  document.getElementById('wholesale').value = html;

  html = table.rows[num - 1].cells.item(9).innerHTML;
  document.getElementById('cost').value = html;

  html = table.rows[num - 1].cells.item(10).innerHTML;
  document.getElementById('taxable').value = html;

  html = table.rows[num - 1].cells.item(11).innerHTML;
  document.getElementById('temple').value = html;

  html = table.rows[num - 1].cells.item(12).innerHTML;
  document.getElementById('size').value = html;

  html = table.rows[num - 1].cells.item(13).innerHTML;
  document.getElementById('bridge').value = html;

  html = table.rows[num - 1].cells.item(14).innerHTML;
  document.getElementById('A').value = html;

  html = table.rows[num - 1].cells.item(15).innerHTML;
  document.getElementById('B').value = html;

  html = table.rows[num - 1].cells.item(16).innerHTML;
  document.getElementById('ED').value = html;

  html = table.rows[num - 1].cells.item(17).innerHTML;
  document.getElementById('DBL').value = html;

  html = table.rows[num - 1].cells.item(18).innerHTML;
  document.getElementById('eye').value = html;

  html = table.rows[num - 1].cells.item(19).innerHTML;
  document.getElementById('VID').value = html;

  html = table.rows[num - 1].cells.item(20).innerHTML;
  document.getElementById('HCFA').value = html;

  html = table.rows[num - 1].cells.item(21).innerHTML;
  document.getElementById('on_order').value = html;

  html = table.rows[num - 1].cells.item(22).innerHTML;
  document.getElementById('reorder_point').value = html;

  html = table.rows[num - 1].cells.item(23).innerHTML;
  document.getElementById('lead_time').value = html;

  html = table.rows[num - 1].cells.item(24).innerHTML;
  document.getElementById('sold_this_week').value = html;

  html = table.rows[num - 1].cells.item(25).innerHTML;
  document.getElementById('sold_this_month').value = html;

  html = table.rows[num - 1].cells.item(26).innerHTML;
  document.getElementById('sold_this_year').value = html;


}
