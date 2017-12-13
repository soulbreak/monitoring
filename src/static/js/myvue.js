var vm = new Vue({
    el: '#applications',
    data:
    {
        applications : [],
    },
    methods: {
        get_data() {
            axios.get('/api/applications')
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
        }

    }
})