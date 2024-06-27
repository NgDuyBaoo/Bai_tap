$(document).ready(function(){
    // Hàm xử lý sự kiện click cho nút "Đăng nhập lại"
    $('#login_again').click(function(event){
      event.preventDefault();
      // Ẩn thông báo lỗi đăng nhập
      $('#note_error_login').hide();
      // Chuyển hướng trang
      window.location.href = '/login/';
    });
  });

  $(document).ready(function(){
    // Hàm xử lý sự kiện click cho nút "Đăng nhập lại"
    $('#create_domain_again').click(function(event){
      event.preventDefault();
      // Ẩn thông báo lỗi đăng nhập
      $('#note_error_create_domain').hide();
    });
  });

  