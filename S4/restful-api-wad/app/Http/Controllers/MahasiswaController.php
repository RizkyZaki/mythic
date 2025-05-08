<?php

namespace App\Http\Controllers;

use App\Models\Mahasiswa;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class MahasiswaController extends Controller
{
    public function index()
    {
        try {
            $mahasiswa = Mahasiswa::all();
            return response()->json([
                'status' => true,
                'statusCode' => 200,
                'message' => 'Data mahasiswa berhasil diambil.',
                'data' => $mahasiswa,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'status' => false,
                'statusCode' => 500,
                'message' => 'Terjadi kesalahan saat mengambil data.',
                'data' => null,
            ], 500);
        }
    }

    public function store(Request $request)
    {
        try {
            $validator = Validator::make($request->all(), [
                'nim' => 'required|max:255|unique:mahasiswa',
                'nama' => 'required|max:255',
                'no_hp' => 'required|max:255',
            ], [
                'nim.required' => 'NIM wajib diisi.',
                'nim.max' => 'NIM tidak boleh lebih dari 255 karakter.',
                'nim.unique' => 'NIM sudah terdaftar.',
                'nama.required' => 'Nama wajib diisi.',
                'nama.max' => 'Nama tidak boleh lebih dari 255 karakter.',
                'no_hp.required' => 'Nomor HP wajib diisi.',
                'no_hp.max' => 'Nomor HP tidak boleh lebih dari 255 karakter.',
            ]);

            if ($validator->fails()) {
                return response()->json([
                    'status' => false,
                    'statusCode' => 400,
                    'message' => $validator->errors()->first(),
                    'data' => null,
                ], 400);
            }

            $mahasiswa = Mahasiswa::create($request->only(['nim', 'nama', 'no_hp']));
            return response()->json([
                'status' => true,
                'statusCode' => 201,
                'message' => 'Data mahasiswa berhasil ditambahkan.',
                'data' => $mahasiswa,
            ], 201);
        } catch (\Exception $e) {
            return response()->json([
                'status' => false,
                'statusCode' => 500,
                'message' => 'Gagal menyimpan data mahasiswa.',
                'data' => null,
            ], 500);
        }
    }

    public function show($id)
    {
        try {
            $mahasiswa = Mahasiswa::findOrFail($id);
            return response()->json([
                'status' => true,
                'statusCode' => 200,
                'message' => 'Data mahasiswa berhasil ditemukan.',
                'data' => $mahasiswa,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'status' => false,
                'statusCode' => 404,
                'message' => 'Data mahasiswa tidak ditemukan.',
                'data' => null,
            ], 404);
        }
    }

    public function update(Request $request, $id)
    {
        try {
            $validator = Validator::make($request->all(), [
                'nim' => 'required|max:255|unique:mahasiswa,nim,' . $id,
                'nama' => 'required|max:255',
                'no_hp' => 'required|max:255',
            ], [
                'nim.required' => 'NIM wajib diisi.',
                'nim.max' => 'NIM tidak boleh lebih dari 255 karakter.',
                'nim.unique' => 'NIM sudah terdaftar.',
                'nama.required' => 'Nama wajib diisi.',
                'nama.max' => 'Nama tidak boleh lebih dari 255 karakter.',
                'no_hp.required' => 'Nomor HP wajib diisi.',
                'no_hp.max' => 'Nomor HP tidak boleh lebih dari 255 karakter.',
            ]);

            if ($validator->fails()) {
                return response()->json([
                    'status' => false,
                    'statusCode' => 400,
                    'message' => $validator->errors()->first(),
                    'data' => null,
                ], 400);
            }

            $mahasiswa = Mahasiswa::findOrFail($id);
            $mahasiswa->update($request->only(['nim', 'nama', 'no_hp']));
            return response()->json([
                'status' => true,
                'statusCode' => 200,
                'message' => 'Data mahasiswa berhasil diperbarui.',
                'data' => $mahasiswa,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'status' => false,
                'statusCode' => 500,
                'message' => 'Gagal memperbarui data mahasiswa.',
                'data' => null,
            ], 500);
        }
    }

    public function destroy($id)
    {
        try {
            $mahasiswa = Mahasiswa::findOrFail($id);
            $mahasiswa->delete();
            return response()->json([
                'status' => true,
                'statusCode' => 200,
                'message' => 'Data mahasiswa berhasil dihapus.',
                'data' => null,
            ], 200);
        } catch (\Exception $e) {
            return response()->json([
                'status' => false,
                'statusCode' => 500,
                'message' => 'Gagal menghapus data mahasiswa.',
                'data' => null,
            ], 500);
        }
    }
}
