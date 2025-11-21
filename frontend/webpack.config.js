const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.jsx', // Webpack will look for the main file here
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      // Rule to handle CSS, including PostCSS/Tailwind
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './index.html', // Use the existing index.html in the frontend root
      filename: 'index.html',
    }),
  ],
  devServer: {
    historyApiFallback: true,
    port: 3000,
    // Proxy requests starting with /api to the Flask backend
    proxy: {
        '/api': 'http://127.0.0.1:5000' 
    }
  },
};