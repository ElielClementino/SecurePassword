FROM node:14.20-slim
WORKDIR /frontend
COPY . .
ENV PORT=3000
RUN npm install
EXPOSE 3000
ENTRYPOINT ["npm", "run", "dev"]