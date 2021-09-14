// Vue用コンポーネント
// ここではマスタッシュ構文が使える

const listComponent = {
    template:`
            <ul>
            <hr>
                <li v-for="log in list">
                    <div>
                    <p>{{ log.store_name }}</p>
                    <p>
                    <span v-if="log.hot">HOT</span>
                    <span v-else>ICE</span>
                    {{ log.product }}￥{{ log.price }}
                    </p>
                    <button @click="select(log.id)">この商品のログを投稿する</button>
                    <hr>
                </div>
                </li>
            </ul>
            `,
    props: {
        "list": Array,
        select: {
            type: Function,
            required: true
        }

    },
}

const postComponent = {
    template: `
        <div>
            <hr>
            <p>Log追加テスト</p>
            <button @click="back">送信せず選択画面に戻る</button>  
            <div>苦味<input type="text" v-model:value="params.bitter"></div>
            <div>酸味<input type="text" v-model:value="params.acidity"></div>
            <div>香り<input type="text" v-model:value="params.smell"></div>
            <div>後味<input type="text" v-model:value="params.after"></div>
            <div>個人的な好み<input type="text" v-model:value="params.likely"></div>
            <div>備考<input type="text" v-model:value="params.note"></div>
            <button @click="post">Log送信</button>
            <p>結果</p>
            <p>{{ message }}</p>
            <p>{{ error }}</p>
            <hr>
        </div>
    `,
    props: {
        'params': Object, 
        'message': String,
        'error': String,
        post: {
            type: Function,
            required: true
        },
        back: {
            type: Function,
            required: true
        }
    }
}