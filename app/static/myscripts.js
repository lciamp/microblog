$("ul.posts li.post").click(function() {
  window.location = $(this).find("a").attr("href");
  return false;
});