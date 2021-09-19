// CSRF設定
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

const api = axios.create({
    // baseURL:"http://127.0.0.1:8000/",
    baseURL:"https://tkuto-coffeelog.herokuapp.com/",
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
});


const app = new Vue({
    el: '#app',

    // マスタッシュ構文のバッティング回避(vue.jsでは ${}と記述)
    delimiters: ["${", "}"],

    // Vueインスタンスマウント後に実行される
    mounted: function () {
        // logのリスト取得API呼び出し
        api({
            method: "get",
            url: "coffeelog/api/coffee",
        })
        .then(function (response) {
            this.receivedData = (response.data)
            console.log(this.receivedData);
        }.bind(this))

        // エラー処理
        .catch(function (error) {
            this.hasError = true;
        }.bind(this))
    },

    methods: {
        addNewUserLog: function(){
                const vm = this;
            api({
                method: "POST",
                url: "userlog/api/new",
                data: this.params,
            })
            .then(function (response) {
                vm.message = response.statusText
                vm.resetParams();
                alert('Logが投稿されました');
            }.bind(this))
            .catch(error =>{
                switch (error.response?.status) {
                    
                    case 400:
                    alert('未入力または規定の値を越えています。')
                    break;

                    default:
                    alert(error)
                }            
            })
        },

        // 送信するLogのidをセット
        setProduct: function(log){
            this.params.product = log.id;
            this.isSelect = true;
            this.selected.name = log.product;
            this.selected.price = log.price;
            this.selected.store = log.store_name;
            this.selected.hot = log.store_hot;
        },

        // Logのidをリセット
        resetProduct: function(){
            this.params.product = null;
            this.isSelect = false;
        },

        resetParams: function(){
            this.resetProduct()
            this.params.bitter = null;
            this.params.acidity = null;
            this.params.smell = null;
            this.params.after = null;
            this.params.likely = null;
            this.params.note = null;
            this.selected.name = null;
            this.selected.store = null;
            this.selected.price = null;
            this.selected.hot = null;
        }
    },

    data: {
        params: {
            product: null,
            bitter: null,
            acidity: null,
            smell: null,
            after: null,
            likely: null,
            note: null,
        },

        selected: {
            name: null,
            store: null,
            price: null,
            hot: null,
        },

        errorMessage: '',
        message: '',
        hasError: false,
        isSelect: false,
        receivedData: null,
    },

    components: {
        'list-component': listComponent,
        'post-component': postComponent,
    }
});