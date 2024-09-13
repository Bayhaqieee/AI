"use strict";

var totalBelanja = 125000;
var jenisMember = "Bronze"; // AND Statement

if (totalBelanja > 100000 && jenisMember == "Silver") {
  console.log("Selamat, Anda mendapat diskon sebesar 10%");
} else {
  console.log("Maaf, saat ini Anda belum mendapat diskon");
} // OR Statement


if (totalBelanja > 100000 || jenisMember == "Silver") {
  console.log("Selamat, Anda mendapat diskon sebesar 10%");
} else {
  console.log("Maaf, saat ini Anda belum mendapat diskon");
}