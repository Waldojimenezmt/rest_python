#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:40:00 2021

@author: waldo
"""
from flask import Flask, request, jsonify, json
from productos import productos

app = Flask(__name__)

@app.route('/api/all')
def all():
    return jsonify(productos)

@app.route('/api/buscar/<string:datos>')
def save(datos):
    ProductoEncontrado = [p for p in productos if p['nombre']==datos]
    if len(ProductoEncontrado)>0:
        productos.append(datos)
        return jsonify({"productos":productos[0]})
    return jsonify({"Error":"No existe!!"})
    
@app.route('/api/save', methods=['POST'])
def savepro():
    nuevo_producto = {
    "id" : request.json['id'],
    "nombre":request.json['nombre'],
    "cantidad":request.json['cantidad'],
    "valor":request.json['valor']
    }
    productos.append(nuevo_producto)
    #return jsonify({"mensaje":"Producto agregado"})
    return jsonify({"mensaje":"Producto almacenado..","productos":productos})

@app.route('/api/update/<string:producto>', methods=['PUT'])
def adicionar(producto):

    posicion = [p for p in productos if p['nombre']==producto]
    if len(posicion)>0:
        productos['id']=request.json[id]
        productos['nombre']=request.json['nombre']
        productos['cantidad']=request.json['cantidad']
        productos['valor']=request.json['valor']
    else:
        return jsonify({'mensaje':'No existe producto'})
if __name__ == '__main__':
    app.run(debug=True, port=8000)

