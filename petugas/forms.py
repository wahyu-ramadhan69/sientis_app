from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from inven.models import *


class BarangForm(forms.ModelForm):
    class Meta:
        model = barang
        fields = ['nama', 'merk', 'jenis',
                  'satuan', 'keterangan', 'Foto', 'kode']

    def __init__(self, *args, **kwargs):
        super(BarangForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'field tidak boleh kosong'.format(
                nama=field.label)}


class jenisbarang(forms.ModelForm):
    class Meta:
        model = jenis
        fields = ['nama', 'deskripsi']


class keranjangbarang(forms.ModelForm):
    class Meta:
        model = keranjang
        fields = ['nama_barang', 'merk_barang', 'jenis_barang', 'id_barang']


class PegawaiForm(forms.ModelForm):
    class Meta:
        model = pegawai
        fields = ['nama', 'nip', 'pangkat',
                  'golongan', 'jabatan', 'Foto']

    def __init__(self, *args, **kwargs):
        super(PegawaiForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'field tidak boleh kosong'.format(
                nama=field.label)}


class statusbarang(forms.ModelForm):
    class Meta:
        model = barang
        fields = ['status', 'keterangan']


class statuspinjam(forms.ModelForm):
    class Meta:
        model = peminjaman_barang
        fields = ['status_peminjaman']


class PinjamBarang(forms.ModelForm):
    class Meta:
        model = peminjaman_barang
        fields = ['nip_peminjam', 'nama_peminjam',
                  'nama_barang', 'status_peminjaman', 'id_barang', 'nama_op']


class KembaliBarang(forms.ModelForm):
    class Meta:
        model = pengembalian_barang
        fields = ['id_transaksi', 'nip_pengembali',
                  'nama_pengembali', 'nama_barang', 'keterangan', 'nama_op', 'kode_pinjam']

    def __init__(self, *args, **kwargs):
        super(KembaliBarang, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'field tidak boleh kosong'.format(
                nip_pengembali=field.label)}
