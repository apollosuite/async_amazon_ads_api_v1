"""Auto-generated models for BrandStorePages from Amazon Ads API v1."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class HorizontalPosition(StrEnum):
    CENTER = "CENTER"  # Center position
    LEFT = "LEFT"  # Left position
    RIGHT = "RIGHT"  # Right position


class StoreBleedImageType(StrEnum):
    ALL = "ALL"  # All sides image bleed
    CORNER = "CORNER"  # Corner image bleed
    NONE = "NONE"  # No image bleed
    SIDE = "SIDE"  # Side image bleed


class StoreCallToActionType(StrEnum):
    BUTTON = "BUTTON"  # Button type call to action
    LINK = "LINK"  # Link type call to action


class StoreColorPalette(StrEnum):
    DEFAULT = "DEFAULT"  # Default color scheme
    DEFAULT_INVERTED = "DEFAULT_INVERTED"  # Inverted default color scheme
    SOLID_BLACK = "SOLID_BLACK"  # Solid black color scheme
    SOLID_WHITE = "SOLID_WHITE"  # Solid white color scheme
    TRANSLUCENT_BLACK = "TRANSLUCENT_BLACK"  # Translucent black color scheme
    TRANSLUCENT_WHITE = "TRANSLUCENT_WHITE"  # Translucent white color scheme
    TRANSPARENT_BLACK = "TRANSPARENT_BLACK"  # Transparent black color scheme
    TRANSPARENT_WHITE = "TRANSPARENT_WHITE"  # Transparent white color scheme


class StoreDealsMode(StrEnum):
    AUTOMATIC = "AUTOMATIC"  # Automatic mode
    BULK = "BULK"  # Bulk mode


class StoreImageLayout(StrEnum):
    CONTAIN = "CONTAIN"  # Contain layout
    COVER = "COVER"  # Cover layout
    TEXT = "TEXT"  # Text layout


class StoreImageShape(StrEnum):
    SQUARE = "SQUARE"  # Square shape


class StoreImageTextAlign(StrEnum):
    LEFT = "LEFT"  # Left text alignment
    RIGHT = "RIGHT"  # Right text alignment


class StoreImageWithTextTileVariation(StrEnum):
    IMAGE_WITH_TEXT = "IMAGE_WITH_TEXT"  # Image with text variation


class StoreLayoutType(StrEnum):
    DEFAULT = "DEFAULT"  # Default layout configuration
    SHOWCASE = "SHOWCASE"  # Showcase layout configuration for featured display


class StorePageTemplate(StrEnum):
    BLANK = "BLANK"  # Empty template for custom layouts
    HIGHLIGHT = "HIGHLIGHT"  # Template for highlighting specific content
    MARQUEE = "MARQUEE"  # Template featuring a prominent marquee section
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"  # Template for displaying collections of products
    PRODUCT_GRID = "PRODUCT_GRID"  # Template displaying products in a grid layout


class StorePageType(StrEnum):
    BRAND_STORE_PAGE = (
        "BRAND_STORE_PAGE"  # Standard brand store page that allows customization to show case the brand and product
    )
    LANDING_PAGE = "LANDING_PAGE"  # Landing page for specific ads program with predefined template


class StoreProductCarouselSearchType(StrEnum):
    BEST_SELLING = "BEST_SELLING"  # Best selling items
    RECOMMENDATION_FOR_YOU = "RECOMMENDATION_FOR_YOU"  # Personalized recommendations


class StoreProductSelectorButtonColor(StrEnum):
    BLACK = "BLACK"  # Black button color
    TRANSPARENT = "TRANSPARENT"  # Transparent button color
    WHITE = "WHITE"  # White button color


class StoreProductSelectorImageLayout(StrEnum):
    BOTTOM = "BOTTOM"  # Bottom image layout
    LEFT = "LEFT"  # Left image layout
    RIGHT = "RIGHT"  # Right image layout
    TOP = "TOP"  # Top image layout


class StoreShoppableTextOption(StrEnum):
    NO_TEXT_UNDER_INTERACTIVE_IMAGE = "NO_TEXT_UNDER_INTERACTIVE_IMAGE"  # No text under interactive image
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"  # Text over interactive image
    TEXT_UNDER_INTERACTIVE_IMAGE = "TEXT_UNDER_INTERACTIVE_IMAGE"  # Text under interactive image


class StoreSlideType(StrEnum):
    ASIN = "ASIN"  # Slide type for StoreASINSlide
    IMAGE = "IMAGE"  # Slide type for StoreGallerySlide, StoreImageSlide


class StoreTextAlignment(StrEnum):
    CENTER = "CENTER"  # Center alignment
    JUSTIFY = "JUSTIFY"  # Justified alignment
    LEFT = "LEFT"  # Left alignment. Default value configured for StoreEmptyTile
    RIGHT = "RIGHT"  # Right alignment


class StoreTextOption(StrEnum):
    TEXT_NEXT_TO_IMAGE = "TEXT_NEXT_TO_IMAGE"  # Text next to image
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"  # Text overlaid on image


class StoreTextOptionType(StrEnum):
    NO_TEXT_OVER_VIDEO = "NO_TEXT_OVER_VIDEO"  # No text overlay on video
    TEXT_OVER_VIDEO = "TEXT_OVER_VIDEO"  # Text overlay on video


class StoreTileBorderSize(StrEnum):
    LARGE = "LARGE"  # Large border size
    MEDIUM = "MEDIUM"  # Medium border size
    NONE = "NONE"  # No border
    SMALL = "SMALL"  # Small border size


class StoreTileSize(StrEnum):
    LARGE = "LARGE"  # Large tile size, StoreAWLSTile only uses LARGE
    MEDIUM = "MEDIUM"  # Medium tile size
    MINI = "MINI"  # Mini tile size
    SMALL = "SMALL"  # Small tile size


class StoreTileTextSize(StrEnum):
    LARGE = "LARGE"  # Large text size
    MEDIUM = "MEDIUM"  # Medium text size
    MINI = "MINI"  # Mini text size
    SMALL = "SMALL"  # Small text size


class StoreTileType(StrEnum):
    CUSTOM_CODE = "CUSTOM_CODE"  # Tile type for StoreCustomCodeTile
    EMPTY = "EMPTY"  # Tile type for StoreEmptyTile
    EXTERNAL_WIDGET = "EXTERNAL_WIDGET"  # Tile type for StoreAWLSTile
    IMAGE = "IMAGE"  # Tile type for StoreImageTile, StoreImageWithTextTile, StoreMetadataItem type
    INTERACTIVE_IMAGE = "INTERACTIVE_IMAGE"  # Tile type for StoreShoppableImageTile
    PRODUCT = "PRODUCT"  # Tile type for StoreProductTile and StoreShoppablePoint type
    TEXT = "TEXT"  # Tile type for StoreTextTile and tile layers
    VIDEO = "VIDEO"  # Tile type for StoreVideoTile


class StoreVerticalAlign(StrEnum):
    BOTTOM = "BOTTOM"  # Bottom alignment
    MIDDLE = "MIDDLE"  # Middle alignment
    TOP = "TOP"  # Top alignment


class StoreWidgetSectionType(StrEnum):
    BANNER = "BANNER"  # Section type for StoreBannerWidget
    BEST_SELLING = "BEST_SELLING"  # Section type for StoreProductCarouselWidget and StoreProductCarouselContent type
    DEALS_AND_COUPONS = "DEALS_AND_COUPONS"  # Section type for StoreDealsWidget and StoreDealsContent type
    EDITORIAL_ROW = "EDITORIAL_ROW"  # Widget type for StoreCustomCodeWidget, StoreImageWithTextWidget, StoreImageWidget, StoreProductWidget, StoreShoppableImageWidget, StoreTextWidget, StoreTileWidget, StoreVideoWidget and StoreAWLSWidget
    GALLERY = "GALLERY"  # Section type for StoreGalleryWidget
    HERO = "HERO"  # Section type for StoreHeroImageWidget
    LIVE_VIDEO = "LIVE_VIDEO"  # Section type for StoreLiveVideoWidget
    MANUALLY_CURATED_PRODUCT_CAROUSEL = "MANUALLY_CURATED_PRODUCT_CAROUSEL"  # Section type for StoreManuallyCuratedProductCarouselWidget and StoreCarouselContent type
    PREMIUM_BEST_SELLING = (
        "PREMIUM_BEST_SELLING"  # Section type for StoreProductCarouselWidget and StoreProductCarouselContent type
    )
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"  # Section type for StoreProductCollectionWidget
    PRODUCT_GRID = "PRODUCT_GRID"  # Section type for StoreProductGridWidget and type for StoreProductCollectionASINGrid
    RECOMMENDED = "RECOMMENDED"  # Section type for StoreProductCarouselWidget and StoreProductCarouselContent type
    SHOP_THE_LOOK_CAROUSEL = (
        "SHOP_THE_LOOK_CAROUSEL"  # Section type for StoreShopTheLookWidget and type for StoreShopTheLookContent
    )


class StoreWidgetType(StrEnum):
    BANNER = "BANNER"  # Widget type and content type for StoreBannerWidget
    EDITORIAL_ROW = "EDITORIAL_ROW"  # Widget type for StoreCustomCodeWidget, StoreImageWithTextWidget, StoreImageWidget, StoreProductWidget, StoreShoppableImageWidget, StoreTextWidget, StoreTileWidget, StoreVideoWidget and StoreAWLSWidget
    GALLERY = "GALLERY"  # Widget type for StoreGalleryWidget and StoreGalleryContent type
    HERO = "HERO"  # Widget type for StoreHeroImageWidget
    LIVE_VIDEO = "LIVE_VIDEO"  # Widget type and content type for StoreLiveVideoWidget
    MULTI_MEDIA_CAROUSEL = "MULTI_MEDIA_CAROUSEL"  # Widget type for StoreShopTheLookWidget, StoreManuallyCuratedProductCarouselWidget and StoreProductCarouselWidget
    PRODUCT_CAROUSEL = "PRODUCT_CAROUSEL"  # Widget type for StoreProductCarouselWidget
    PRODUCT_COLLECTION = (
        "PRODUCT_COLLECTION"  # Widget type for StoreProductCollectionWidget and StoreProductCollection type
    )
    PRODUCT_GRID = "PRODUCT_GRID"  # Widget type for StoreProductGridWidget and StoreDealsWidget


class VerticalPosition(StrEnum):
    BOTTOM = "BOTTOM"  # Bottom position
    MIDDLE = "MIDDLE"  # Middle position
    TOP = "TOP"  # Top position


class BrandStorePage(LenientModel):
    content: StorePageContent
    editionId: str = Field(description="Reference to the store edition")
    pageId: str = Field(description="Unique identifier for the store page")
    pageType: Annotated[StorePageType | str, lenient_enum(StorePageType)]
    storeEditionPublishId: str | None = Field(
        default=None, description="Optional identifier for the published version of this page"
    )
    storeId: str = Field(description="Identifier of the associated store")


class BrandStorePageBrandStoreEditionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStorePageBrandStoreEditionPublishVersionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStorePageBrandStoreIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStorePagePageIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStorePageSuccessResponse(LenientModel):
    brandStorePages: list[BrandStorePage] | None = Field(default=None, min_length=0, max_length=50)
    nextToken: str | None = Field(default=None)


class BrandedRecipeDirection(LenientModel):
    """Represents a single step in a recipe's directions"""

    body: str = Field(description="Detailed instruction text for the direction step")
    title: str = Field(description="Title or heading for the direction step")


class BrandedRecipeIngredient(LenientModel):
    """Represents an ingredient in a branded recipe"""

    asinOverrides: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ASIN overrides for the ingredient"
    )
    brand: str = Field(description="Brand name associated with the ingredient")
    displayText: str = Field(description="Formatted text for displaying the ingredient")
    isAsinRestricted: bool = Field(description="Flag indicating if ASIN is restricted for this ingredient")
    isBrandRestricted: bool = Field(description="Flag indicating if brand is restricted for this ingredient")
    isExclusiveOverride: bool = Field(description="Flag indicating if this ingredient has exclusive override")
    name: str = Field(description="Name of the ingredient")
    quantityList: list[BrandedRecipeQuantityItem] | None = Field(
        default=None, min_length=0, max_length=500, description="List of quantity measurements for the ingredient"
    )


class BrandedRecipeIngredientsMetadata(LenientModel):
    """Contains metadata information for recipe ingredients"""

    priorityAsins: list[PriorityAsin] | None = Field(
        default=None,
        min_length=0,
        max_length=500,
        description="List of priority ASINs for ingredients with detailed product information",
    )
    quantity: float | None = Field(default=None, description="Quantity amount for the ingredient")
    searchText: str | None = Field(default=None, description="Search text for ingredient metadata")
    translatedUnit: str | None = Field(default=None, description="Translated unit of measurement")


class BrandedRecipeMedia(LenientModel):
    """Represents media content associated with a recipe"""

    altText: str | None = Field(default=None, description="Alternative text description of the media content")
    assetLibraryId: str | None = Field(default=None, description="Identifier for the asset.")
    mediaUrl: str | None = Field(default=None, description="URL of the media content")


class BrandedRecipeQuantityItem(LenientModel):
    """Represents a quantity measurement for a recipe ingredient"""

    amount: float = Field(description="Numerical amount of the ingredient")
    unit: str = Field(description="Unit of measurement for the ingredient")


class BrandedRecipeWidget(LenientModel):
    """Main widget structure for displaying a branded recipe"""

    availableProductAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of available product ASINs."
    )
    desktopMedia: BrandedRecipeMedia | None = Field(default=None)
    directions: list[BrandedRecipeDirection] | None = Field(
        default=None, min_length=0, max_length=500, description="List of preparation directions for the recipe"
    )
    encodedIngredientComposition: str | None = Field(
        default=None, description="Encoded string containing ingredient composition details"
    )
    ingredientMetadata: list[BrandedRecipeIngredientsMetadata] | None = Field(
        default=None, min_length=0, max_length=500, description="Metadata associated with recipe ingredients"
    )
    ingredients: list[BrandedRecipeIngredient] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ingredients required for the recipe"
    )
    isInitialLoad: bool | None = Field(default=None, description="Flag indicating if recipe is set to initial load")
    mobileMedia: BrandedRecipeMedia | None = Field(default=None)
    preparationTime: str = Field(description="Time required to prepare the recipe")
    refTag: str | None = Field(default=None, description="REF tracking tag for the branded recipe")
    servingSize: float = Field(description="Number of servings the recipe yields")
    title: str | None = Field(default=None, description="Title of the recipe")


class CTI(LenientModel):
    category: str | None = Field(default=None, description="Category identifier.")
    item: str | None = Field(default=None, description="Item identifier.")
    type: str | None = Field(default=None, description="Type identifier.")


class CommonTileProperties(LenientModel):
    size: Annotated[StoreTileSize | str, lenient_enum(StoreTileSize)]
    tag: str = Field(description="The unique tag for the tile to help track on performance.")
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)]


class CommonWidgetProperties(LenientModel):
    sectionType: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]
    widgetTag: str = Field(description="The unique tag for the widget to help track on performance.")
    widgetType: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)]


class Coordinates(LenientModel):
    x: float | None = Field(default=None, description="X coordinate.")
    y: float | None = Field(default=None, description="Y coordinate.")


class PriorityAsin(LenientModel):
    """Product information for a priority ASIN"""

    addToCartActionParams: str = Field(description="Parameters for add to cart action")
    bottleDepositFee: str | None = Field(default=None, description="Bottle deposit fee amount")
    bottleDepositFeeString: str | None = Field(default=None, description="Bottle deposit fee as string")
    cartQuantity: float = Field(description="Quantity of this item in the cart")
    catalogDisplayPricePerUnitOfMeasure: str | None = Field(
        default=None, description="Price per unit of measure for display"
    )
    freshButton: str | None = Field(default=None, description="Fresh button information")
    isAlternateSearchResult: bool = Field(description="Flag indicating if this is an alternate search result")
    isRequiredQuantityInCart: bool = Field(description="Flag indicating if a quantity is required in cart")
    isSoldByCount: bool = Field(description="Flag indicating if the product is sold by count")
    itemAvailability: str = Field(description="Status of item availability")
    offerId: str = Field(description="Unique identifier for the offer")
    offerName: str = Field(description="Display name of the product offer")
    offerUnit: str = Field(description="Unit of the offer (e.g., Fl Oz, lb)")
    productAsin: str = Field(description="ASIN associated with this product")
    productDetailsUrl: str = Field(description="URL to the product details page")
    productImageUrl: str = Field(description="URL of the product image")
    promotionDisplay: str | None = Field(default=None, description="Display text for active promotion")
    promotionId: str | None = Field(default=None, description="Identifier for active promotion")
    quantityInStock: float | None = Field(default=None, description="Available quantity in stock")
    requiredQuantity: float = Field(description="Required quantity for purchase")
    retailATCButton: str | None = Field(default=None, description="Retail add-to-cart button information")
    reviewStars: ReviewStars | None = Field(default=None)
    searchTerm: str | None = Field(default=None, description="Search term associated with this product")
    subtotalParams: str = Field(description="Subtotal parameters for pricing calculations")
    vuomDisplayPrice: str = Field(description="Display price for virtual unit of measure")


class QueryBrandStorePageRequest(StrictModel):
    editionIdFilter: BrandStorePageBrandStoreEditionIdFilter
    maxResults: int | None = Field(default=50, ge=1, le=50)
    nextToken: str | None = Field(default=None)
    pageIdFilter: BrandStorePagePageIdFilter
    storeEditionPublishIdFilter: BrandStorePageBrandStoreEditionPublishVersionIdFilter | None = Field(default=None)
    storeIdFilter: BrandStorePageBrandStoreIdFilter


class ReviewStars(LenientModel):
    """Review information for a product"""

    hasHalfStar: bool = Field(description="Flag indicating if the product has a half star in the rating")
    reviewCount: int = Field(description="Number of reviews for the product")
    wholeStars: int = Field(description="Number of whole stars in the rating")


class StoreASINSlide(LenientModel):
    productAsin: str = Field(description="The ASIN of the product.")
    tag: str = Field(description="Unique tag for the slide which will be ASIN.")
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)]


class StoreAWLSTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreAWLSTileContent | None = Field(default=None)
    externalWidgetId: str = Field(description="External widget identifier.")


class StoreAWLSTileContentBrandedRecipeWidget(LenientModel):
    brandedRecipeWidget: BrandedRecipeWidget


class StoreAWLSTileContentStoreProductSelectorWidget(LenientModel):
    storeProductSelectorWidget: StoreProductSelectorWidget


class StoreAWLSTileContentStoreVideoRevealWidget(LenientModel):
    storeVideoRevealWidget: StoreVideoRevealWidget


type StoreAWLSTileContent = StoreAWLSTileContentBrandedRecipeWidget | StoreAWLSTileContentStoreProductSelectorWidget | StoreAWLSTileContentStoreVideoRevealWidget


class StoreAWLSWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreAWLSTile] = Field(
        min_length=1, max_length=1, description="The AWLS tile configuration. Exactly one tile is required."
    )
    widgetDependencies: list[str] | None = Field(
        default=None, min_length=0, max_length=10, description="List of widget dependencies."
    )


class StoreBannerContent(LenientModel):
    banners: StoreBanners | None = Field(default=None)
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = Field(default=None)


class StoreBannerWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreBannerContent


class StoreBanners(LenientModel):
    blackLivesMatter: bool = Field(description="Flag to display Black Lives Matter banner")
    stopAsianHate: bool = Field(description="Flag to display Stop Asian Hate banner")


class StoreCallToActionData(LenientModel):
    customUrl: str | None = Field(default=None, description="Custom URL for the call to action.")
    pageId: str | None = Field(default=None, description="Page identifier.")
    productAsin: str | None = Field(default=None, description="ASIN for the call to action.")
    text: str | None = Field(default=None, description="Call to action text.")


class StoreCallToActionProductData(LenientModel):
    customUrl: str | None = Field(default=None, description="Custom URL for the call to action.")
    productAsin: str | None = Field(default=None, description="Product ASIN for the call to action.")
    text: str | None = Field(default=None, description="Call to action text.")


class StoreCanvasData(LenientModel):
    canvasHeight: float | None = Field(default=None, description="Height in the canvas.")
    height: float | None = Field(default=None, description="Height in the canvas.")
    left: float | None = Field(default=None, description="Left position in the canvas.")
    naturalHeight: float | None = Field(default=None, description="Natural height of the image.")
    naturalWidth: float | None = Field(default=None, description="Natural width of the image.")
    top: float | None = Field(default=None, description="Top position in the canvas.")
    width: float | None = Field(default=None, description="Width in the canvas.")


class StoreCarouselContent(LenientModel):
    bulk: bool = Field(description="Whether this is a bulk configuration.")
    callToActionData: StoreCallToActionData
    includeOutOfStock: bool = Field(description="Whether to include out of stock items.")
    keyword: str = Field(description="Keyword for product filtering.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ASINs, maximum 500 unique items."
    )
    search: StoreCarouselSearch | None = Field(default=None)
    slides: list[StoreASINSlide] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ASIN slides."
    )
    tag: str = Field(description="Unique tag for the content to track performance.")
    text: str = Field(description="Description text.")
    title: str = Field(description="Title of the carousel.")
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]


class StoreCarouselSearch(LenientModel):
    includeOutOfStock: bool = Field(description="Whether to include out of stock items in search.")
    keyword: str = Field(description="Search keyword.")
    node: str = Field(description="Node identifier for search.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="List of ASINs for search filtering."
    )


class StoreCropBoxData(LenientModel):
    height: float | None = Field(default=None, description="Height of the crop box.")
    left: float | None = Field(default=None, description="Left position of the crop box.")
    top: float | None = Field(default=None, description="Top position of the crop box.")
    width: float | None = Field(default=None, description="Width of the crop box.")


class StoreCroppedImage(LenientModel):
    altText: str | None = Field(default=None, description="Alternative text for the image.")
    assetId: str | None = Field(default=None, description="Asset identifier.")
    canvasData: StoreCanvasData | None = Field(default=None)
    cropBox: StoreCropBoxData | None = Field(default=None)
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageNaturalHeight: float | None = Field(default=None, description="Natural height of the image.")
    imageNaturalWidth: float | None = Field(default=None, description="Natural width of the image.")
    imageUrl: str | None = Field(default=None, description="URL of the image.")


class StoreCustomCodeContent(LenientModel):
    autoDimension: bool | None = Field(default=None, description="Whether to use automatic dimensioning.")
    availableProductAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of available ASINs, maximum 500 unique items."
    )
    cti: CTI | None = Field(default=None)
    embedCode: str | None = Field(default=None, description="Embedded code content.")
    integrity: str | None = Field(default=None, description="Integrity hash for security.")
    widgetName: str | None = Field(default=None, description="Name of the widget.")
    widgetTag: str | None = Field(default=None, description="Widget identifier.")


class StoreCustomCodeTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreCustomCodeContent | None = Field(default=None)


class StoreCustomCodeWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreCustomCodeTile] = Field(
        min_length=1, max_length=1, description="The custom code tile configuration. Exactly one tile is required."
    )


class StoreDealsConfig(LenientModel):
    node: str | None = Field(default=None, description="Node identifier for deals.")


class StoreDealsContent(LenientModel):
    deals: StoreDealsConfig | None = Field(default=None)
    dealsMode: Annotated[StoreDealsMode | str, lenient_enum(StoreDealsMode)] | None = Field(default=None)
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ASINs, maximum 500 unique items."
    )
    tag: str | None = Field(default=None, description="Unique tag for the content to track performance.")
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)] | None = Field(default=None)


class StoreDealsWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreDealsContent | None = Field(default=None)


class StoreEmptyTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreEmptyTileContent


class StoreEmptyTileContent(LenientModel):
    bondCustomerServiceLink: bool | None = Field(
        default=None, description="Whether to include a customer service link."
    )
    callToAction: str | None = Field(default=None, description="Call to action text.")
    text: str | None = Field(default=None, description="Text content (must be empty).")
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(default=None)
    title: str | None = Field(default=None, description="Title of the tile (must be empty).")


class StoreGalleryContent(LenientModel):
    metadata: list[StoreMetadataItem] | None = Field(
        default=None, min_length=0, max_length=15, description="Metadata associated with the gallery."
    )
    slides: list[StoreGallerySlide] | None = Field(
        default=None, min_length=0, max_length=15, description="List of slides in the gallery."
    )
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    text: str | None = Field(default=None, description="Text content of the gallery.")
    title: str | None = Field(default=None, description="Title of the gallery.")
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = Field(default=None)


class StoreGallerySlide(LenientModel):
    alt: str | None = Field(default=None, description="Alternative text for the slide.")
    assetId: str | None = Field(default=None, description="Asset identifier for the slide.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)] | None = Field(default=None)


class StoreGalleryWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreGalleryContent | None = Field(default=None)


class StoreHeroContent(LenientModel):
    assetId: str | None = Field(default=None, description="Identifier for the asset.")
    assetTags: str | None = Field(default=None, description="Tags associated with the asset.")
    canvasData: StoreCanvasData | None = Field(default=None)
    description: str | None = Field(default=None, description="Description of the hero image.")
    imageHeight: float | None = Field(default=None, description="Height of the hero image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset of the image.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset of the image.")
    imageUrl: str = Field(description="URL of the hero image.")
    imageWidth: float | None = Field(default=None, description="Width of the hero image.")
    mobileContent: StoreMobileContent | None = Field(default=None)
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    textOverlay: str | None = Field(default=None, description="Text overlay displayed on the hero image.")


class StoreHeroImageWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreHeroContent | None = Field(default=None)


class StoreImageContent(LenientModel):
    altText: str | None = Field(default=None, description="Alternative text for the image.")
    assetId: str | None = Field(default=None, description="Asset identifier.")
    assetTags: str | None = Field(default=None, description="Tags associated with the asset.")
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = Field(default=None)
    callToAction: str | None = Field(default=None, description="Call to action text.")
    canvasData: StoreCanvasData | None = Field(default=None)
    cropBoxData: StoreCropBoxData | None = Field(default=None)
    customUrl: str | None = Field(default=None, description="Custom URL.")
    hideTitle: bool | None = Field(default=None, description="Whether to hide the title.")
    imageHeight: float | None = Field(default=None, description="Height of the image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the image.")
    imageWidth: float | None = Field(default=None, description="Width of the image.")
    isAiGen: bool | None = Field(default=None, description="Whether the image is AI-generated.")
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = Field(default=None)
    pageId: str | None = Field(default=None, description="Page identifier.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the image."
    )
    text: str | None = Field(default=None, description="Text content.")
    textAlign: Annotated[StoreImageTextAlign | str, lenient_enum(StoreImageTextAlign)] | None = Field(default=None)
    tileLayers: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Layer configuration for the tile."
    )
    title: str | None = Field(default=None, description="Title of the image.")
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = Field(default=None)


class StoreImageSlide(LenientModel):
    assetId: str | None = Field(default=None, description="Asset identifier.")
    assetTags: str | None = Field(default=None, description="Tags associated with the asset.")
    canvasData: StoreCanvasData | None = Field(default=None)
    imageHeight: float | None = Field(default=None, description="Height of the image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the image.")
    imageWidth: float | None = Field(default=None, description="Width of the image.")
    tag: str | None = Field(default=None, description="Unique identifier for the slide.")
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)] | None = Field(default=None)


class StoreImageTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreImageContent | None = Field(default=None)
    flexHeight: bool | None = Field(default=None, description="Whether the height is flexible.")
    mobileContent: StoreMobileImageContent | None = Field(default=None)
    uploadMobileImage: bool | None = Field(default=None, description="Whether to upload a mobile-specific image.")


class StoreImageWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreImageTile] = Field(
        min_length=1, max_length=1, description="The image tile configuration. Exactly one tile is required."
    )


class StoreImageWithTextContent(LenientModel):
    altText: str | None = Field(default=None, description="Alternative text for the image.")
    assetId: str | None = Field(default=None, description="Asset identifier.")
    assetTags: str | None = Field(default=None, description="Tags associated with the asset.")
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = Field(default=None)
    callToAction: str | None = Field(default=None, description="Call to action text.")
    canvasData: StoreCanvasData | None = Field(default=None)
    cropBoxData: StoreCropBoxData | None = Field(default=None)
    customUrl: str | None = Field(default=None, description="Custom URL.")
    hideTitle: bool | None = Field(default=None, description="Whether to hide the title.")
    imageHeight: float | None = Field(default=None, description="Height of the image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the image.")
    imageWidth: float | None = Field(default=None, description="Width of the image.")
    isAiGen: bool | None = Field(default=None, description="Whether the image is AI-generated.")
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = Field(default=None)
    pageId: str | None = Field(default=None, description="Page identifier.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the image."
    )
    renderTileLayers: bool | None = Field(default=None, description="Whether to render tile layers.")
    shape: Annotated[StoreImageShape | str, lenient_enum(StoreImageShape)] | None = Field(default=None)
    text: str | None = Field(default=None, description="Text content.")
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(default=None)
    textOption: Annotated[StoreTextOption | str, lenient_enum(StoreTextOption)] | None = Field(default=None)
    tileLayers: list[StoreTileLayer] | None = Field(
        default=None, min_length=0, max_length=1, description="Layer configuration for the tile."
    )
    title: str | None = Field(default=None, description="Title of the image.")
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = Field(default=None)


class StoreImageWithTextTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreImageWithTextContent | None = Field(default=None)
    flexHeight: bool | None = Field(default=None, description="Whether the height is flexible.")
    mobileContent: StoreMobileImageWithTextContent | None = Field(default=None)
    uploadMobileImage: bool | None = Field(default=None, description="Whether to upload a mobile-specific image.")
    variation: Annotated[StoreImageWithTextTileVariation | str, lenient_enum(StoreImageWithTextTileVariation)]


class StoreImageWithTextWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreImageWithTextTile] = Field(
        min_length=1, max_length=1, description="The image with text tile configuration. Exactly one tile is required."
    )


class StoreLiveVideoContent(LenientModel):
    channel: str | None = Field(default=None, description="Channel of the video.")
    tag: str = Field(description="Unique tag for the content.")
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)]


class StoreLiveVideoWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreLiveVideoContent


class StoreManuallyCuratedProductCarouselWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreCarouselContent | None = Field(default=None)


class StoreMetadataItem(LenientModel):
    alt: str | None = Field(default=None, description="Alternative text.")
    assetId: str | None = Field(default=None, description="Asset identifier.")
    filename: str | None = Field(default=None, description="Name of the file.")
    imageKey: str | None = Field(default=None, description="Key identifier for the image.")
    imageUrl: str | None = Field(default=None, description="The imageUrl of the item.")
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = Field(default=None)
    url: str | None = Field(default=None, description="URL of the item.")


class StoreMobileContent(LenientModel):
    assetId: str | None = Field(default=None, description="Asset identifier for mobile view.")
    assetTags: str | None = Field(default=None, description="Asset tags for mobile view.")
    canvasData: StoreCanvasData | None = Field(default=None)
    imageHeight: float | None = Field(default=None, description="Height of the image for mobile view.")
    imageKey: str | None = Field(default=None, description="Image key for mobile view.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset of the image for mobile view.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset of the image for mobile view.")
    imageUrl: str | None = Field(default=None, description="URL of the image for mobile view.")
    imageWidth: float | None = Field(default=None, description="Width of the image for mobile view.")
    version: str | None = Field(default=None, description="Version identifier for mobile content")


class StoreMobileImageContent(LenientModel):
    altText: str | None = Field(default=None, description="Alternative text for the mobile image.")
    assetId: str | None = Field(default=None, description="Asset identifier for mobile.")
    assetTags: str | None = Field(default=None, description="Tags associated with the mobile asset.")
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = Field(default=None)
    canvasData: StoreCanvasData | None = Field(default=None)
    cropBoxData: StoreCropBoxData | None = Field(default=None)
    hideTitle: bool | None = Field(default=None, description="Whether to hide the title on mobile.")
    imageHeight: float | None = Field(default=None, description="Height of the mobile image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the mobile image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for mobile image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for mobile image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the mobile image.")
    imageWidth: float | None = Field(default=None, description="Width of the mobile image.")
    isAiGen: bool | None = Field(default=None, description="Whether the mobile image is AI-generated.")
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = Field(default=None)
    tileLayers: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Layer configuration for the mobile tile."
    )
    title: str | None = Field(default=None, description="Title for mobile display.")
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = Field(default=None)


class StoreMobileImageWithTextContent(LenientModel):
    altText: str | None = Field(default=None, description="Alternative text for the mobile image.")
    assetId: str | None = Field(default=None, description="Asset identifier for mobile.")
    assetTags: str | None = Field(default=None, description="Tags associated with the mobile asset.")
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = Field(default=None)
    canvasData: StoreCanvasData | None = Field(default=None)
    cropBoxData: StoreCropBoxData | None = Field(default=None)
    hideTitle: bool | None = Field(default=None, description="Whether to hide the title on mobile.")
    imageHeight: float | None = Field(default=None, description="Height of the mobile image.")
    imageKey: str | None = Field(default=None, description="Key identifier for the mobile image.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for mobile image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for mobile image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the mobile image.")
    imageWidth: float | None = Field(default=None, description="Width of the mobile image.")
    isAiGen: bool | None = Field(default=None, description="Whether the mobile image is AI-generated.")
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = Field(default=None)
    renderTileLayers: bool | None = Field(default=None, description="Whether to render tile layers on mobile.")
    shape: Annotated[StoreImageShape | str, lenient_enum(StoreImageShape)] | None = Field(default=None)
    text: str | None = Field(default=None, description="Text content for mobile.")
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(default=None)
    textOption: Annotated[StoreTextOption | str, lenient_enum(StoreTextOption)] | None = Field(default=None)
    tileLayers: list[StoreTileLayer] | None = Field(
        default=None, min_length=0, max_length=1, description="Layer configuration for the mobile tile."
    )
    title: str | None = Field(default=None, description="Title for mobile display.")
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = Field(default=None)


class StorePageContent(LenientModel):
    """Structure containing the content elements of a store page"""

    description: str | None = Field(default=None, description="Description of the page")
    template: Annotated[StorePageTemplate | str, lenient_enum(StorePageTemplate)]
    title: str | None = Field(
        default=None, description="For store page, title of the page; for SB landing page, this can be optional"
    )
    widgets: list[StorePageWidget] | None = Field(
        default=None, min_length=0, max_length=20, description="Collection of widgets displayed on the page"
    )


class StorePageWidgetStoreHeroImageWidget(LenientModel):
    storeHeroImageWidget: StoreHeroImageWidget


class StorePageWidgetStoreTileWidget(LenientModel):
    storeTileWidget: StoreTileWidget


class StorePageWidgetStoreImageWidget(LenientModel):
    storeImageWidget: StoreImageWidget


class StorePageWidgetStoreTextWidget(LenientModel):
    storeTextWidget: StoreTextWidget


class StorePageWidgetStoreImageWithTextWidget(LenientModel):
    storeImageWithTextWidget: StoreImageWithTextWidget


class StorePageWidgetStoreProductCollectionWidget(LenientModel):
    storeProductCollectionWidget: StoreProductCollectionWidget


class StorePageWidgetStoreProductGridWidget(LenientModel):
    storeProductGridWidget: StoreProductGridWidget


class StorePageWidgetStoreDealsWidget(LenientModel):
    storeDealsWidget: StoreDealsWidget


class StorePageWidgetStoreProductWidget(LenientModel):
    storeProductWidget: StoreProductWidget


class StorePageWidgetStoreShoppableImageWidget(LenientModel):
    storeShoppableImageWidget: StoreShoppableImageWidget


class StorePageWidgetStoreCustomCodeWidget(LenientModel):
    storeCustomCodeWidget: StoreCustomCodeWidget


class StorePageWidgetStoreVideoWidget(LenientModel):
    storeVideoWidget: StoreVideoWidget


class StorePageWidgetStoreGalleryWidget(LenientModel):
    storeGalleryWidget: StoreGalleryWidget


class StorePageWidgetStoreShopTheLookWidget(LenientModel):
    storeShopTheLookWidget: StoreShopTheLookWidget


class StorePageWidgetStoreManuallyCuratedProductCarouselWidget(LenientModel):
    storeManuallyCuratedProductCarouselWidget: StoreManuallyCuratedProductCarouselWidget


class StorePageWidgetStoreAwlsWidget(LenientModel):
    storeAWLSWidget: StoreAWLSWidget


class StorePageWidgetStoreBannerWidget(LenientModel):
    storeBannerWidget: StoreBannerWidget


class StorePageWidgetStoreProductCarouselWidget(LenientModel):
    storeProductCarouselWidget: StoreProductCarouselWidget


class StorePageWidgetStoreLiveVideoWidget(LenientModel):
    storeLiveVideoWidget: StoreLiveVideoWidget


type StorePageWidget = StorePageWidgetStoreHeroImageWidget | StorePageWidgetStoreTileWidget | StorePageWidgetStoreImageWidget | StorePageWidgetStoreTextWidget | StorePageWidgetStoreImageWithTextWidget | StorePageWidgetStoreProductCollectionWidget | StorePageWidgetStoreProductGridWidget | StorePageWidgetStoreDealsWidget | StorePageWidgetStoreProductWidget | StorePageWidgetStoreShoppableImageWidget | StorePageWidgetStoreCustomCodeWidget | StorePageWidgetStoreVideoWidget | StorePageWidgetStoreGalleryWidget | StorePageWidgetStoreShopTheLookWidget | StorePageWidgetStoreManuallyCuratedProductCarouselWidget | StorePageWidgetStoreAwlsWidget | StorePageWidgetStoreBannerWidget | StorePageWidgetStoreProductCarouselWidget | StorePageWidgetStoreLiveVideoWidget


class StoreProductCarouselContent(LenientModel):
    callToActionData: StoreCallToActionProductData | None = Field(default=None)
    searchContent: StoreProductCarouselSearch | None = Field(default=None)
    tag: str = Field(description="Unique tag for the content.")
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]


class StoreProductCarouselSearch(LenientModel):
    node: str | None = Field(default=None, description="Node identifier for search")
    type: Annotated[StoreProductCarouselSearchType | str, lenient_enum(StoreProductCarouselSearchType)] | None = Field(
        default=None
    )


class StoreProductCarouselWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreProductCarouselContent


class StoreProductCollectionASINGrid(LenientModel):
    bulk: bool | None = Field(default=None, description="Whether this is a bulk configuration.")
    description: str | None = Field(default=None, description="Description of the product grid.")
    displayProductGridHeader: bool | None = Field(
        default=None, description="Whether to display the product grid header."
    )
    includeOutOfStock: bool | None = Field(default=None, description="Whether to include out of stock products.")
    isAutomatedProductGrid: bool | None = Field(
        default=None, description="Whether the product grid is automatically populated"
    )
    keyword: str | None = Field(default=None, description="Keyword for product filtering.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=60, description="List of ASINs, maximum 60 unique items."
    )
    sort: str | None = Field(default=None, description="Sort order for products.")
    tag: str | None = Field(default=None, description="Unique tag for the tile to track performance.")
    title: str | None = Field(default=None, description="Title of the product grid.")
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]
    variation: str | None = Field(default=None, description="Variation of the product grid.")


class StoreProductCollectionContent(LenientModel):
    collectionTags: str | None = Field(default=None, description="Tags associated with the collection.")
    productGridConversionTimestamp: float | None = Field(
        default=None, description="Timestamp of product grid conversion."
    )
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = Field(default=None)


class StoreProductCollectionImageTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreImageWithTextContent | None = Field(default=None)
    flexHeight: bool | None = Field(default=None, description="Whether the height is flexible.")
    mobileContent: StoreMobileImageWithTextContent | None = Field(default=None)
    uploadMobileImage: bool | None = Field(default=None, description="Whether to upload a mobile-specific image.")
    variation: Annotated[StoreImageWithTextTileVariation | str, lenient_enum(StoreImageWithTextTileVariation)]


class StoreProductCollectionTileStoreProductCollectionImageTile(LenientModel):
    storeProductCollectionImageTile: StoreProductCollectionImageTile


class StoreProductCollectionTileStoreProductCollectionAsinGrid(LenientModel):
    storeProductCollectionASINGrid: StoreProductCollectionASINGrid


type StoreProductCollectionTile = StoreProductCollectionTileStoreProductCollectionImageTile | StoreProductCollectionTileStoreProductCollectionAsinGrid


class StoreProductCollectionWidget(LenientModel):
    aiMetadata: list[Tag] | None = Field(
        default=None, min_length=0, max_length=1000, description="Metadata about AI generated fields."
    )
    commonProperties: CommonWidgetProperties
    content: StoreProductCollectionContent | None = Field(default=None)
    tiles: list[StoreProductCollectionTile] = Field(
        min_length=2, max_length=2, description="The tiles for the product collection. Exactly two tiles are required."
    )


class StoreProductGridContent(LenientModel):
    bulk: bool | None = Field(default=None, description="Whether this is a bulk product grid.")
    description: str | None = Field(default=None, description="Description of the product grid.")
    displayProductGridHeader: bool | None = Field(default=None, description="Whether to display the grid header.")
    excludedProductAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of product ASINs exclude when dynamic."
    )
    includeOutOfStock: bool | None = Field(default=None, description="Whether to include out of stock products.")
    isAutomatedProductGrid: bool | None = Field(
        default=None, description="Whether the product grid is automatically populated"
    )
    keyword: str | None = Field(default=None, description="Keyword for product filtering.")
    pinnedProductAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=25, description="List of product ASINs include when dynamic."
    )
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of product ASINs."
    )
    productType: str | None = Field(default=None, description="Type of products to display")
    search: StoreProductGridSearch | None = Field(default=None)
    showOnlyMarkdown: bool | None = Field(default=None, description="Whether to only show products on markdown.")
    sort: str | None = Field(default=None, description="Sort order for products.")
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    title: str | None = Field(default=None, description="Title of the product grid.")
    type: str | None = Field(default=None, description="Type of the content.")


class StoreProductGridSearch(LenientModel):
    brandId: str | None = Field(default=None, description="brand id to search.")
    includeOutOfStock: bool | None = Field(
        default=None, description="Whether to include out of stock products in search."
    )
    keyword: str | None = Field(default=None, description="Search keyword.")
    node: str | None = Field(default=None, description="Node identifier for search.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of product ASINs."
    )
    sort: str | None = Field(default=None, description="Sort order for search results.")


class StoreProductGridWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreProductGridContent


class StoreProductSelectorAnswer(LenientModel):
    """Represents a possible answer in the product selector questionnaire"""

    image: StoreProductSelectorImage | None = Field(default=None)
    nextStep: str = Field(description="Reference to the next question or step in the selection flow")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="List of ASINs associated with this answer"
    )
    tag: str = Field(description="Unique identifier for the answer")
    text: str | None = Field(default=None, description="Display text for the answer option")


class StoreProductSelectorDesignOptions(LenientModel):
    """Visual styling options for the product selector widget"""

    backgroundColor: str = Field(description="Background color in hex or named color value")
    backgroundShape: str = Field(description="Shape of the background container")
    buttonColor: (
        Annotated[StoreProductSelectorButtonColor | str, lenient_enum(StoreProductSelectorButtonColor)] | None
    ) = Field(default=None)
    buttonShape: str = Field(description="Shape style for buttons in the selector")
    textAlignment: str = Field(description="Alignment of text elements (left, center, right)")
    textSize: str = Field(description="Size of the text elements")
    textStyle: str = Field(description="Font family or style to be used")
    textWeight: str = Field(description="Font weight for text elements")


class StoreProductSelectorImage(LenientModel):
    """Represents an image used in the product selector introduction"""

    assetId: str = Field(description="Asset ID of the image")
    fileName: str | None = Field(default=None, description="File name of the image")
    imageUrl: str = Field(description="URL of the image")
    layout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)] | None = (
        Field(default=None)
    )


class StoreProductSelectorImageOptions(LenientModel):
    """Image options for the product selector introduction"""

    image: StoreProductSelectorImage
    layoutConfiguration: StoreProductSelectorLayoutConfiguration


class StoreProductSelectorIntroduction(LenientModel):
    """Introduction section for the product selector widget"""

    buttonText: str = Field(description="Text displayed on the introduction button")
    description: str = Field(description="Description text for the introduction section")
    heading: str = Field(description="Heading text for the introduction section")
    headline: str | None = Field(default=None, description="Headline text for the introduction section")
    imageOptions: StoreProductSelectorImageOptions
    isEnabled: bool = Field(description="Flag indicating whether the introduction is enabled")


class StoreProductSelectorLayoutConfiguration(LenientModel):
    """Layout configuration for desktop and mobile views"""

    desktopLayout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)]
    mobileLayout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)]


class StoreProductSelectorQuestion(LenientModel):
    """Represents a question in the product selector questionnaire"""

    answerList: list[StoreProductSelectorAnswer] | None = Field(
        default=None, min_length=0, max_length=500, description="List of possible answers for this question"
    )
    areImagesEnabled: bool | None = Field(default=None, description="Flag indicating whether images are enabled")
    description: str | None = Field(default=None, description="Additional descriptive text or context for the question")
    hasImage: bool | None = Field(default=None, description="Flag indicating whether the question has an image")
    tag: str = Field(description="Unique identifier for the question")
    text: str | None = Field(default=None, description="Main question text displayed to the user")


class StoreProductSelectorResults(LenientModel):
    """Configuration for displaying product selector results"""

    buttonText: str | None = Field(default=None, description="Text to display on the call-to-action button")
    description: str | None = Field(default=None, description="Descriptive text explaining the results")
    disclaimer: str = Field(description="Legal or additional information text for the results")
    headline: str = Field(description="Main heading text for the results section")
    storeUrl: str | None = Field(default=None, description="URL to the store page for the selected products")


class StoreProductSelectorWidget(LenientModel):
    """Main widget structure for the product selector feature"""

    designOptions: StoreProductSelectorDesignOptions
    introduction: StoreProductSelectorIntroduction | None = Field(default=None)
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=500, description="Master list of ASINs available in the selector"
    )
    questionList: list[StoreProductSelectorQuestion] | None = Field(
        default=None, min_length=0, max_length=500, description="Ordered list of questions in the selector flow"
    )
    results: StoreProductSelectorResults


class StoreProductTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreProductTileContent | None = Field(default=None)


class StoreProductTileContent(LenientModel):
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = Field(default=None)
    displayOutOfStockASIN: bool | None = Field(default=None, description="Whether to display out of stock ASIN.")
    layout: Annotated[StoreLayoutType | str, lenient_enum(StoreLayoutType)] | None = Field(default=None)
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the product."
    )
    text: str | None = Field(default=None, description="Description text for the product.")
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(default=None)
    title: str | None = Field(default=None, description="Title of the product.")


class StoreProductWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreProductTile] = Field(
        min_length=1, max_length=1, description="The product tile configuration. Exactly one tile is required."
    )


class StoreShopTheLookContent(LenientModel):
    bulk: bool | None = Field(default=None, description="Whether this is a bulk configuration.")
    callToActionData: StoreCallToActionData | None = Field(default=None)
    includeOutOfStock: bool | None = Field(default=None, description="Whether to include out of stock items.")
    keyword: str | None = Field(default=None, description="Keyword for searching.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=25, description="List of product ASINs, maximum 25 unique items."
    )
    search: StoreShopTheLookSearch | None = Field(default=None)
    slides: list[StoreShopTheLookSlide] | None = Field(
        default=None, min_length=0, max_length=500, description="List of slides in the carousel."
    )
    tag: str | None = Field(default=None, description="Unique tag for the content.")
    text: str | None = Field(default=None, description="Text content.")
    title: str | None = Field(default=None, description="Title of the content.")
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)] | None = Field(default=None)


class StoreShopTheLookSearch(LenientModel):
    includeOutOfStock: bool | None = Field(default=None, description="Whether to include out of stock items in search.")
    keyword: str | None = Field(default=None, description="Search keyword.")
    node: str | None = Field(default=None, description="Node identifier for search.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for search filtering."
    )


class StoreShopTheLookSlideStoreImageSlide(LenientModel):
    storeImageSlide: StoreImageSlide


class StoreShopTheLookSlideStoreAsinSlide(LenientModel):
    storeASINSlide: StoreASINSlide


type StoreShopTheLookSlide = StoreShopTheLookSlideStoreImageSlide | StoreShopTheLookSlideStoreAsinSlide


class StoreShopTheLookWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    content: StoreShopTheLookContent | None = Field(default=None)


class StoreShoppableImageContent(LenientModel):
    croppedImage: StoreCroppedImage | None = Field(default=None)
    points: list[StoreShoppablePoint] | None = Field(
        default=None, min_length=0, max_length=6, description="Interactive points on the image."
    )
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the point."
    )
    renderTileLayers: bool | None = Field(default=None, description="Whether to render tile layers.")
    textOption: Annotated[StoreShoppableTextOption | str, lenient_enum(StoreShoppableTextOption)] | None = Field(
        default=None
    )
    tileLayers: list[StoreTileLayer] | None = Field(
        default=None, min_length=0, max_length=1, description="Layer configuration for the tile."
    )


class StoreShoppableImageTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreShoppableImageContent | None = Field(default=None)


class StoreShoppableImageWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreShoppableImageTile] = Field(
        min_length=1, max_length=1, description="The shoppable image tile configuration. Exactly one tile is required."
    )


class StoreShoppablePoint(LenientModel):
    coordinates: Coordinates
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the point."
    )
    tag: str | None = Field(default=None, description="Unique tag for the point.")
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = Field(default=None)


class StoreTextContent(LenientModel):
    bold: bool = Field(description="Whether text should be bold.")
    bondCustomerServiceLink: bool | None = Field(default=None, description="Whether to include customer service link.")
    callToAction: str | None = Field(default=None, description="Call to action text.")
    customUrl: str | None = Field(default=None, description="Custom URL for the content.")
    pageId: str | None = Field(default=None, description="Identifier for the page.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single product ASIN for the content."
    )
    text: str = Field(description="Main text content.")
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(default=None)
    title: str = Field(description="Title of the content.")
    uppercase: bool = Field(description="Whether text should be uppercase.")


class StoreTextTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreTextContent | None = Field(default=None)


class StoreTextWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreTextTile] = Field(min_length=1, max_length=1, description="Single text tile configuration.")


class StoreTileStoreImageWithTextTile(LenientModel):
    storeImageWithTextTile: StoreImageWithTextTile


class StoreTileStoreImageTile(LenientModel):
    storeImageTile: StoreImageTile


class StoreTileStoreProductTile(LenientModel):
    storeProductTile: StoreProductTile


class StoreTileStoreShoppableImageTile(LenientModel):
    storeShoppableImageTile: StoreShoppableImageTile


class StoreTileStoreTextTile(LenientModel):
    storeTextTile: StoreTextTile


class StoreTileStoreVideoTile(LenientModel):
    storeVideoTile: StoreVideoTile


class StoreTileStoreEmptyTile(LenientModel):
    storeEmptyTile: StoreEmptyTile


class StoreTileStoreCustomCodeTile(LenientModel):
    storeCustomCodeTile: StoreCustomCodeTile


type StoreTile = StoreTileStoreImageWithTextTile | StoreTileStoreImageTile | StoreTileStoreProductTile | StoreTileStoreShoppableImageTile | StoreTileStoreTextTile | StoreTileStoreVideoTile | StoreTileStoreEmptyTile | StoreTileStoreCustomCodeTile


class StoreTileLayer(LenientModel):
    colorPalette: Annotated[StoreColorPalette | str, lenient_enum(StoreColorPalette)] | None = Field(default=None)
    content: StoreTileLayerContent | None = Field(default=None)
    coverTile: bool | None = Field(default=None, description="Whether the layer covers the entire tile.")
    margin: Annotated[StoreTileBorderSize | str, lenient_enum(StoreTileBorderSize)] | None = Field(default=None)
    opacity: float | None = Field(default=None, description="Opacity level of the layer.")
    outOfBounds: bool | None = Field(default=None, description="Whether the layer is out of bounds.")
    padding: Annotated[StoreTileBorderSize | str, lenient_enum(StoreTileBorderSize)] | None = Field(default=None)
    position: StoreTilePosition | None = Field(default=None)
    tag: str | None = Field(default=None, description="Unique tag for the tile layer to track performance.")
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = Field(default=None)


class StoreTileLayerContent(LenientModel):
    bodyText: str | None = Field(default=None, description="Body text for the layer.")
    bondCustomerServiceLink: bool | None = Field(
        default=None, description="Whether to include a customer service link."
    )
    callToAction: str | None = Field(default=None, description="Call to action text for the layer.")
    callToActionType: Annotated[StoreCallToActionType | str, lenient_enum(StoreCallToActionType)] | None = Field(
        default=None
    )
    customUrl: str | None = Field(default=None, description="Custom URL for the layer.")
    headerText: str | None = Field(default=None, description="Header text for the layer.")
    pageId: str | None = Field(default=None, description="Page identifier for the layer.")
    prefixText: str | None = Field(default=None, description="Prefix text for the layer.")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="Single ASIN for the layer."
    )
    tileTextAlignment: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = Field(
        default=None
    )
    tileTextSize: Annotated[StoreTileTextSize | str, lenient_enum(StoreTileTextSize)] | None = Field(default=None)


class StoreTilePosition(LenientModel):
    x: Annotated[HorizontalPosition | str, lenient_enum(HorizontalPosition)] | None = Field(default=None)
    y: Annotated[VerticalPosition | str, lenient_enum(VerticalPosition)] | None = Field(default=None)


class StoreTileWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    rowHeight: int | None = Field(default=None, description="Height of the row in pixels.")
    tiles: list[StoreTile] = Field(
        min_length=2, max_length=8, description="The tiles for the widget. Minimum 2 and maximum 8 tiles are allowed."
    )


class StoreVideoContent(LenientModel):
    assetId: str | None = Field(default=None, description="Asset identifier.")
    assetTags: str | None = Field(default=None, description="Tags associated with the asset.")
    autoPlay: bool | None = Field(default=None, description="Whether video should auto-play.")
    callToAction: str | None = Field(default=None, description="Call to action text.")
    canvasData: StoreCanvasData | None = Field(default=None)
    customUrl: str | None = Field(default=None, description="Custom URL for the content.")
    imageHeight: float | None = Field(default=None, description="Height of the image.")
    imageKey: str | None = Field(default=None, description="Key for the image asset.")
    imageOffsetLeft: float | None = Field(default=None, description="Left offset for image positioning.")
    imageOffsetTop: float | None = Field(default=None, description="Top offset for image positioning.")
    imageUrl: str | None = Field(default=None, description="URL of the image.")
    imageWidth: float | None = Field(default=None, description="Width of the image.")
    mute: bool | None = Field(default=None, description="Whether video should be muted.")
    pageId: str | None = Field(default=None, description="Page identifier")
    productAsins: list[str] | None = Field(
        default=None, min_length=0, max_length=1, description="List of product ASINs."
    )
    renderTileLayers: bool | None = Field(default=None, description="Whether to render tile layers.")
    resourceId: str | None = Field(default=None, description="Resource identifier.")
    text: str | None = Field(default=None, description="Text content.")
    textAlign: str | None = Field(default=None, description="Text alignment.")
    textOption: Annotated[StoreTextOptionType | str, lenient_enum(StoreTextOptionType)] | None = Field(default=None)
    tileLayers: list[StoreTileLayer] | None = Field(
        default=None, min_length=0, max_length=1, description="Configuration for tile layers."
    )
    title: str | None = Field(default=None, description="Title of the content.")
    videoAssetId: str | None = Field(default=None, description="Video asset identifier.")
    videoAssetTags: str | None = Field(default=None, description="Tags associated with the video asset.")
    videoDescription: str | None = Field(default=None, description="Description of the video.")
    videoKey: str | None = Field(default=None, description="Key for the video asset.")
    videoName: str | None = Field(default=None, description="Name of the video.")
    videoSize: float | None = Field(default=None, description="Size of the video in bytes.")
    videoUrl: str | None = Field(default=None, description="URL of the video.")


class StoreVideoRevealVRVideo(LenientModel):
    """Configuration for a single video reveal video asset"""

    assetId: str = Field(description="Unique identifier for the video asset")
    url: str = Field(description="URL of the video content")


class StoreVideoRevealVideos(LenientModel):
    """Collection of video assets for different device types"""

    desktop: StoreVideoRevealVRVideo
    mobile: StoreVideoRevealVRVideo


class StoreVideoRevealWidget(LenientModel):
    """Main widget structure for the video reveal feature"""

    backgroundColor: str = Field(description="Background color (CSS property)")
    csmTag: str = Field(description="CSM tracking tag for the video reveal")
    fadeoutDuration: str = Field(description="Fadeout duration (in ms)")
    objectFit: str = Field(description="Object fit (CSS property)")
    skipReveal: bool = Field(description="Skip reveal (to be used in development only)")
    throttleLimit: str = Field(description="Play video every X minutes")
    videos: StoreVideoRevealVideos


class StoreVideoTile(LenientModel):
    commonProperties: CommonTileProperties
    content: StoreVideoContent | None = Field(default=None)


class StoreVideoWidget(LenientModel):
    commonProperties: CommonWidgetProperties
    tiles: list[StoreVideoTile] = Field(
        min_length=1, max_length=1, description="The content configuration for the video widget."
    )


class Tag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


__all__ = [
    "BrandStorePage",
    "BrandStorePageBrandStoreEditionIdFilter",
    "BrandStorePageBrandStoreEditionPublishVersionIdFilter",
    "BrandStorePageBrandStoreIdFilter",
    "BrandStorePagePageIdFilter",
    "BrandStorePageSuccessResponse",
    "BrandedRecipeDirection",
    "BrandedRecipeIngredient",
    "BrandedRecipeIngredientsMetadata",
    "BrandedRecipeMedia",
    "BrandedRecipeQuantityItem",
    "BrandedRecipeWidget",
    "CTI",
    "CommonTileProperties",
    "CommonWidgetProperties",
    "Coordinates",
    "HorizontalPosition",
    "PriorityAsin",
    "QueryBrandStorePageRequest",
    "ReviewStars",
    "StoreASINSlide",
    "StoreAWLSTile",
    "StoreAWLSTileContent",
    "StoreAWLSWidget",
    "StoreBannerContent",
    "StoreBannerWidget",
    "StoreBanners",
    "StoreBleedImageType",
    "StoreCallToActionData",
    "StoreCallToActionProductData",
    "StoreCallToActionType",
    "StoreCanvasData",
    "StoreCarouselContent",
    "StoreCarouselSearch",
    "StoreColorPalette",
    "StoreCropBoxData",
    "StoreCroppedImage",
    "StoreCustomCodeContent",
    "StoreCustomCodeTile",
    "StoreCustomCodeWidget",
    "StoreDealsConfig",
    "StoreDealsContent",
    "StoreDealsMode",
    "StoreDealsWidget",
    "StoreEmptyTile",
    "StoreEmptyTileContent",
    "StoreGalleryContent",
    "StoreGallerySlide",
    "StoreGalleryWidget",
    "StoreHeroContent",
    "StoreHeroImageWidget",
    "StoreImageContent",
    "StoreImageLayout",
    "StoreImageShape",
    "StoreImageSlide",
    "StoreImageTextAlign",
    "StoreImageTile",
    "StoreImageWidget",
    "StoreImageWithTextContent",
    "StoreImageWithTextTile",
    "StoreImageWithTextTileVariation",
    "StoreImageWithTextWidget",
    "StoreLayoutType",
    "StoreLiveVideoContent",
    "StoreLiveVideoWidget",
    "StoreManuallyCuratedProductCarouselWidget",
    "StoreMetadataItem",
    "StoreMobileContent",
    "StoreMobileImageContent",
    "StoreMobileImageWithTextContent",
    "StorePageContent",
    "StorePageTemplate",
    "StorePageType",
    "StorePageWidget",
    "StoreProductCarouselContent",
    "StoreProductCarouselSearch",
    "StoreProductCarouselSearchType",
    "StoreProductCarouselWidget",
    "StoreProductCollectionASINGrid",
    "StoreProductCollectionContent",
    "StoreProductCollectionImageTile",
    "StoreProductCollectionTile",
    "StoreProductCollectionWidget",
    "StoreProductGridContent",
    "StoreProductGridSearch",
    "StoreProductGridWidget",
    "StoreProductSelectorAnswer",
    "StoreProductSelectorButtonColor",
    "StoreProductSelectorDesignOptions",
    "StoreProductSelectorImage",
    "StoreProductSelectorImageLayout",
    "StoreProductSelectorImageOptions",
    "StoreProductSelectorIntroduction",
    "StoreProductSelectorLayoutConfiguration",
    "StoreProductSelectorQuestion",
    "StoreProductSelectorResults",
    "StoreProductSelectorWidget",
    "StoreProductTile",
    "StoreProductTileContent",
    "StoreProductWidget",
    "StoreShopTheLookContent",
    "StoreShopTheLookSearch",
    "StoreShopTheLookSlide",
    "StoreShopTheLookWidget",
    "StoreShoppableImageContent",
    "StoreShoppableImageTile",
    "StoreShoppableImageWidget",
    "StoreShoppablePoint",
    "StoreShoppableTextOption",
    "StoreSlideType",
    "StoreTextAlignment",
    "StoreTextContent",
    "StoreTextOption",
    "StoreTextOptionType",
    "StoreTextTile",
    "StoreTextWidget",
    "StoreTile",
    "StoreTileBorderSize",
    "StoreTileLayer",
    "StoreTileLayerContent",
    "StoreTilePosition",
    "StoreTileSize",
    "StoreTileTextSize",
    "StoreTileType",
    "StoreTileWidget",
    "StoreVerticalAlign",
    "StoreVideoContent",
    "StoreVideoRevealVRVideo",
    "StoreVideoRevealVideos",
    "StoreVideoRevealWidget",
    "StoreVideoTile",
    "StoreVideoWidget",
    "StoreWidgetSectionType",
    "StoreWidgetType",
    "Tag",
    "VerticalPosition",
]
