const { defineConfig } = require('@vue/cli-service')


module.exports = {
  transpileDependencies: true,
  // devServer: {
  //   proxy: {
  //     '/api': {
  //       target: 'https://www.koreaexim.go.kr',
  //       changeOrigin: true,
  //       pathRewrite: {
  //         '^/api': '/site/program/financial/exchangeJSON',
  //       },
  //     },
  //   },
  // },
}
