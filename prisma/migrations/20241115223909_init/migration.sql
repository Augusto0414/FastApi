-- CreateTable
CREATE TABLE "Todito" (
    "id" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "completed" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "Todito_pkey" PRIMARY KEY ("id")
);
