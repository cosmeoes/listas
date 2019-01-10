$(document).ready(function () {
  $('#formUrl').submit(function (event) {
    event.preventDefault();
    $(event.target).prop("disable", true);
    $("#formats").html('')
    $("#title").html('Loading download options...');
    $.post('list_formats/', $('#formUrl').serialize(), function (data) {
      if(data.error) {
        $("#title").html(data.error);
        return;
      }
      $("#title").html(data.title);
      data.streams.forEach(function (stream) {
        $(event.target).prop("disable", false);
        $("#formats").append(
          `
            <div class='card text-center'>
              <div class='card-body'>
                <h5 class='card-title'>
                  Quality: ${stream.resolution}/${stream.fps}fps
                </h5>
                <p>Size: ${humanFileSize(stream.filesize)}</p>
                <a href="${escapeHtml(stream.url)}">Download</a>
              </div>
            </div>
          `)
      });

    })
  });
});

function escapeHtml(html){
  var text = document.createTextNode(html);
  var p = document.createElement('p');
  p.appendChild(text);
  return p.innerHTML;
}

function humanFileSize(bytes) {
    var thresh = 1024;
    if(Math.abs(bytes) < thresh) {
        return bytes + ' B';
    }
    var units = ['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB'];
    var u = -1;
    do {
        bytes /= thresh;
        ++u;
    } while(Math.abs(bytes) >= thresh && u < units.length - 1);
    return bytes.toFixed(1)+' '+units[u];
}
