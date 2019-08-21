
new Vue({
    el: '#vue-app',
    data: {
        greeting: "Hello human.",
        name: 'Steve',
        status: "Working on website...",
        json_data: {}
    },
    methods: {
        greet: (time) => {
            return `Good ${time} ${this.name}!`;
            // return "Good " + time + " " + this.name + " !";
        },
        fetchData: async() => {
            var data = await fetch("https://1cc0d8af.ngrok.io/current-data").then(news => {
                return news.json()
            })
            console.log(data.articles)
            this.json_data = JSON.stringify(data)
        }
    }
})