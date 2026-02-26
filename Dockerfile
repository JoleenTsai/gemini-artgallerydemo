# Use a Node.js 20 base image
FROM node:20-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the working directory
COPY src/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY src/ .

# The 'serve' package defaults to port 3000
ENV PORT 3000
EXPOSE $PORT

# Start the application
CMD ["npm", "start"]
