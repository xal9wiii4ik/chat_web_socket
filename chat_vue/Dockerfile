# build stage
FROM node:lts-alpine as build-stage
WORKDIR /chat_vue
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build