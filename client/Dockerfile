# Use the official Node.js image as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json (if using npm) to the container
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy all the client app files to the container
COPY . .

# Build the app
RUN npm run build

# Set the environment variable for React production build
ENV NODE_ENV=production

# Expose the port your React app is running on (if you are using a different port, replace 3000 with your port number)
EXPOSE 3000

# Command to start the app
CMD ["npm", "start"]
