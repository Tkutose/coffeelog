// CSRF設定
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

const api = axios.create({
    baseURL:"http://127.0.0.1:8000/",
    // baseURL:"https://tkuto-coffeelog.herokuapp.com/",
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
        }.bind(this))

        // エラー処理
        .catch(function (error) {
            this.hasError = true;
        }.bind(this))
    },

    methods: {
        addNewUserLog: function(){
            // 入力値のバリデーション
            if (this.validate()){
                const vm = this;
                
                api({
                    method: "POST",
                    url: "userlog/api/new",
                    data: this.params,
                })
                .then(function (response) {
                    vm.message = response.statusText
                    vm.resetParams();
                    console.log(response.status);
                    alert('Logが投稿されました');
                }.bind(this))
                .catch(error =>{
                    switch (error.response?.status) {
                        case 429:
                        alert('１日に送信できる上限に達しました。また翌日お試しください。')
                        vm.resetParams();
                        break;

                        default:
                        alert(error)
                    }            
                })
            } else {
                // バリデーションでエラー
                alert('未入力または規定の値を越えているものがあります。備考以外の値は1~5で入力してください。')
            }
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

        // paramsとselectedをリセット
        resetParams: function(){
            this.resetProduct();
            for (const param in this.params) {
                this.params[param] = null;
            }
            for (const param in this.selected) {
                this.selected[param] = null;
            }
        },
        
        // 入力値のチェック
        validate: function(){
            flag = true
            checkParams = ['bitter', 'acidity', 'smell', 'after', 'likely'];
            for (const param of checkParams) {
                if(this.params[param] == null){
                    flag = false;
                }
                if(this.params[param] > 5){
                    flag = false;
                }
            }
            return flag;
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