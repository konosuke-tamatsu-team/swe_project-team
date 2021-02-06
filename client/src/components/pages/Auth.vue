<template>
    <v-container grid-list-md>
        <v-layout row wrap align-center justify-center fill-height>
            <v-flex xs12 sm8 lg4 md5>
                <v-card class="login-card" v-if="step === 0">
                    <v-card-title>
                    <span class="headline">Login to 社会福祉士国家試験攻略アプリ</span>
                    </v-card-title>
                    <v-spacer/>
                    <v-card-text>
                    <v-layout
                        row
                        fill-height
                        justify-center
                        align-center
                        v-if="loading"
                    >
                        <v-progress-circular
                        :size="50"
                        color="primary"
                        indeterminate
                        />
                    </v-layout>
                    <v-form v-else ref="form" v-model="valid" lazy-validation>
                        <v-container>

                        <v-text-field
                            v-model="credentials.username"
                            :counter="70"
                            label="ユーザー名"
                            :rules="rules.username"
                            maxlength="70"
                            required
                        />
                        <v-text-field
                            type="password"
                            v-model="credentials.password"
                            :counter="20"
                            label="パスワード"
                            :rules="rules.password"
                            maxlength="20"
                            required
                        />
                        </v-container>
                        <v-btn class="pink white--text" :disabled="!valid" @click="login">Login</v-btn>
                    </v-form>
                    </v-card-text>
                    <p v-on:click="step=1">新規会員登録</p>
                </v-card>









                <v-card class="login-card" v-if="step === 1">
                    <v-card-title>
                    <span class="headline">新規会員登録</span>
                    </v-card-title>
                    <v-spacer/>
                    <v-card-text>
                    <v-layout
                        row
                        fill-height
                        justify-center
                        align-center
                        v-if="loading"
                    >
                        <v-progress-circular
                        :size="50"
                        color="primary"
                        indeterminate
                        />
                    </v-layout>
                    <v-form v-else ref="form" v-model="valid" lazy-validation>
                        <v-container>

                        <v-text-field
                            v-model="credentials_allAuth.username"
                            :counter="70"
                            label="ユーザー名"
                            :rules="rules.username"
                            maxlength="70"
                            required
                        />
                        <v-text-field
                            type="email"
                            v-model="credentials_allAuth.email"
                            :counter="20"
                            label="email"
                            :rules="rules.email"
                            maxlength="20"
                            required
                        />
                        <v-text-field
                            type="password"
                            v-model="credentials_allAuth.password1"
                            :counter="20"
                            label="パスワード"
                            :rules="rules.password"
                            maxlength="20"
                            required
                        />
                        <v-text-field
                            type="password"
                            v-model="credentials_allAuth.password2"
                            :counter="20"
                            label="パスワード"
                            :rules="rules.password"
                            maxlength="20"
                            required
                        />
                        </v-container>
                        <v-btn class="pink white--text" :disabled="!valid" @click="createUser()">createAccount()</v-btn>
                    </v-form>
                    </v-card-text>
                    <p v-on:click="step=0">ログイン画面へ</p>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import router from '../../router';
export default {
    name: 'Auth',
    data: () => ({
        credentials: {},
        credentials_allAuth: {},
        valid:true,
        loading:false,
        step:0,
        rules: {
        username: [
            v => !!v || "ユーザー名は必須です",
            v => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
            v => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
        ],
        password: [
            v => !!v || "パスワードは必須です",
            v => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません"
        ]
        }
    }),
    methods: {
        login() {
            if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8080/auth/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/');
            // eslint-disable-next-line
            }).catch(e => {
                this.loading = false;
                Swal.fire({
                type: 'warning',
                title: 'Error',
                text: 'ユーザー名もしくはパスワード、または両方が間違っています',
                showConfirmButton:false,
                showCloseButton:false,
                timer:3000
                })
            })
            }
        },
        createUser() {
            if (this.$refs.form.validate()) {
            this.loading = true;
            console.log(this.credentials_allAuth)
            axios.post('http://localhost:8080/api/v1/rest-auth/registration/', this.credentials_allAuth).then(res => {
                alert(1)
                this.$session.start();
                alert(2)
                this.$session.set('token', res.data.token);
                alert(3)
                router.push('/');
                alert(4)
            // eslint-disable-next-line
            }).catch(e => {
                this.loading = false;
                Swal.fire({
                type: 'warning',
                title: 'Error',
                text: 'ユーザー名もしくはパスワード、または両方が間違っています',
                showConfirmButton:false,
                showCloseButton:false,
                timer:3000
                })
            })
            }
        },
        s() {
            //alert(1)
            //401だから認証されてないことが原因か？？http://localhost:8000/api/
            axios.post('http://localhost:8080/api/v1/rest-auth/registration/').then(response => (this.info = response["data"])
            // eslint-disable-next-line
            ).catch(e => {
                 console.log(e)
            })
        },
        createAccount() {
            if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8080/auth/users/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/');
            // eslint-disable-next-line
            }).catch(e => {
                this.loading = false;
                Swal.fire({
                type: 'warning',
                title: 'Error',
                text: 'ユーザー名もしくはパスワード、または両方が間違っています',
                showConfirmButton:false,
                showCloseButton:false,
                timer:3000
                })
            })
            }
        }
    }
}
</script>