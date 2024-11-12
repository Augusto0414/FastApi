# Etapa 1: Construcción del proyecto
FROM node:18 AS builder

WORKDIR /app

# Copia los archivos de configuración de dependencias
COPY package.json package-lock.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos del proyecto
COPY . .

# Ejecuta la construcción del proyecto
RUN npm run build

# Etapa 2: Servidor de producción
FROM node:18-alpine

WORKDIR /app

# Copia los archivos construidos desde la etapa anterior
COPY --from=builder /app/dist /app

# Expone el puerto de la app
EXPOSE 3000

# Sirve la app construida en producción
CMD ["npx", "serve", "-s", ".", "-l", "3000"]
