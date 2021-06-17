# Specify a base image
FROM node:alpine

# Setup the container's working directory
WORKDIR /usr/app

# Install some package dependencies
COPY ./package.json ./
RUN npm install

# Copy working files
COPY ./ ./

# Default command
CMD [ "npm", "start" ]