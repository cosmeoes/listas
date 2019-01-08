$(document).ready(function () {
  $('#modalItem').on('shown.bs.modal', function (e) {
    let listaId = $(e.relatedTarget).data('lista-id');
    $(".modal-footer > .btn-primary").off('click');
    $(".modal-footer > .btn-primary").click(function () {
      $(this).prop('disabled', true);
      agregarItem(listaId);
    })
    $('#inputItem').val('');
    $('#inputItem').trigger('focus');
  })
  $('#modalItem').on('hidden.bs.modal', function (e) {
    $('#inputItem').val('');
    $(".modal-footer > .btn-primary").off('click');
  });

  $("#inputItem").keydown(function(event) {
    if (event.keyCode === 13) {
        $(".modal-footer > .btn-primary").click();
    }
});
});

function marcarHecho(id) {
  $.ajax({
      url: "toogle_cross/"+id,
      success: function (result) {
        $("#item"+id+" > div").toggleClass('crossed');
        $("#item"+id+" > .btn-warning").html($("#item"+id+" > .btn-warning").html() == 'Hecho' ? 'No hecho' : 'Hecho');
      },
      error: function (err) {
        console.log(err);
      }
    });
}

function borrarItem(id) {
  $.ajax({
      url: "delete_item/"+id,
      success: function (result) {
        div = $("#item"+id).parent();
        $("#item"+id).remove();
        console.log(div.children())
        if(div.children().length < 1) {
          div.html('');
        }
      },
      error: function (err) {
        console.log(err);
      }
    });
}

function agregarItem(listaId) {
  $.post("add_item/"+listaId, { nombre: $("#inputItem").val(), csrfmiddlewaretoken: CSRF_TOKEN }, function(res) {
    console.log(res)
    if(res.errores) {
      res.errores.forEach(function(error) {
        $('#modalItem .modal-body > .text-danger').append(error)
      });
    } else {
      console.log('appending');
      let clase = res.crusado ? 'crossed': '';
      let texto = res.crusado ? 'No hecho': 'Hecho';
      $("#itemsLista"+listaId).prepend(
        `
        <div id="item${res.id}">
        <div class="${clase}">
        ${res.nombre}
        </div>
        <button onclick="marcarHecho(${res.id})" type="button" class="btn btn-warning" name="button">${texto}</button>
        <button onclick="borrarItem(${res.id})" type="button" class="btn btn-danger" name="button">Borrar</button>
        </div>
        `
      );
      $('#modalItem').modal('hide');
    }
    $(".modal-footer > .btn-primary").prop('disabled', false);
  })
  .fail(function(err) {
    console.log(err);
  })
}

function borrarLista(id) {
  $.ajax({
      url: "delete_lista/"+id,
      success: function (result) {
        div = $("#lista"+id).parent();
        $("#lista"+id).remove();
        console.log(div.children())
        if(div.children().length < 1) {
          div.html('');
        }
      },
      error: function (err) {
        console.log(err);
      }
    });
}
