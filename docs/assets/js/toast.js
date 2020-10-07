const now = new Date();
const expire = new Date(2019, 0, 31);

if (now<=expire){
    $(document).ready(function(){
        $('.toast').toast('show');
    });
}