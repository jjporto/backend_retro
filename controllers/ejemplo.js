const cloudinary = require('../config/cloudinary');

const uploadImage = async (file) => {
    const result = await cloudinary.uploader.upload(file.path);
    return result.secure_url;
};

module.exports = { uploadImage };
